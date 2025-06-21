#!/usr/bin/env zsh
# estimate-s3-storage.zsh
# Quick-n-dirty tally of S3 storage across multiple AWS accounts
# Requires: ada CLI, AWS CLI v2, bc

set -euo pipefail

buckets_file=${1:-buckets.txt}
[[ -r "$buckets_file" ]] || { echo "File $buckets_file not found"; exit 1; }

typeset -F total_bytes=0   # floating point accumulator

while read -r account bucket; do
  [[ -z "$account" || -z "$bucket" ]] && continue

  echo "\n▶︎ ${account}/${bucket}"

  # 1. Assume short-lived creds for the target account
  ada credentials update \
      --account "${account}" \
      --provider conduit \
      --role IibsAdminAccess-DO-NOT-DELETE \
      --once

  # 2. Discover bucket region (us-east-1 if LocationConstraint is null)
  region=$(aws s3api get-bucket-location --bucket "${bucket}" \
           --query 'LocationConstraint' --output text 2>/dev/null)
  [[ "$region" == "None" || -z "$region" ]] && region="us-east-1"

  # 3. Pull the most recent daily BucketSizeBytes datapoint
  size_bytes=$(aws cloudwatch get-metric-statistics \
      --namespace AWS/S3 \
      --metric-name BucketSizeBytes \
      --dimensions Name=BucketName,Value="${bucket}" \
                   Name=StorageType,Value=StandardStorage \
      --start-time "$(date -u -v-3d +%Y-%m-%dT%H:%M:%SZ)" \
      --end-time   "$(date -u      +%Y-%m-%dT%H:%M:%SZ)" \
      --period 86400 \
      --statistics Average \
      --region "${region}" \
      --query 'Datapoints | sort_by(@,&Timestamp)[-1].Average' \
      --output text 2>/dev/null)

  if [[ "$size_bytes" == "None" || -z "$size_bytes" ]]; then
    echo "   ⚠️  No CloudWatch metric found (new bucket or not yet published)"
    continue
  fi

  # 4. Print bucket size in GiB
  size_gib=$(printf "%.2f" "$(bc -l <<<"${size_bytes}/1024/1024/1024")")
  echo "   Size ≈ ${size_gib} GiB"

  # 5. Add to running total
  total_bytes=$(bc -l <<<"${total_bytes}+${size_bytes}")
done < "$buckets_file"

total_gib=$(printf "%.2f" "$(bc -l <<<"${total_bytes}/1024/1024/1024")")
echo "\n────────────────────────────────────────────"
echo "Grand total ≈ ${total_gib} GiB"
