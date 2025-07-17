#!/usr/bin/env zsh
# state‑json‑builder.sh
# Interactive helper for generating or updating state.json used by app.py
set -euo pipefail

###############################################
#  Prerequisites
###############################################
# 1. jq (https://stedolan.github.io/jq/) must be on PATH.
# 2. This script lives next to app.py; state.json is written in that directory.
###############################################

# Ensure jq is available
command -v jq >/dev/null || {
  echo "❌  jq is required but not found. Install jq and retry." >&2
  exit 1
}

# Resolve locations
SCRIPT_DIR="${0:a:h}"
STATE_FILE="$SCRIPT_DIR/state.json"

# If the state file is missing, start with an empty object
[[ -f "$STATE_FILE" ]] || echo '{}' > "$STATE_FILE"

# Helper to pull saved defaults
get_default() {
  jq -r --arg key "$1" 'if .[$key] then .[$key] else "" end' "$STATE_FILE"
}

# Generic prompt helper
#   ask <prompt> <default> <validator‑regex (optional)>
ask() {
  local prompt="$1" default="$2" re="${3:-}" value
  while true; do
    if [[ -n "$default" ]]; then
      read "value?$prompt [$default]: "
      [[ -z "$value" ]] && value="$default"
    else
      read "value?$prompt: "
    fi
    [[ -z "$re" || "$value" =~ $re ]] && { echo "$value"; return; }
    echo "  ↳ Invalid value – please try again."
  done
}

###############################################
#  Collect user input (with validation)
###############################################
ACCOUNT_ID=$( ask "What is the AWS account ID (12 digits) that you want to store these S3 logs in?"           "$(get_default account_id)"        '^[0-9]{12}$'            )
REGION=$(     ask "What is the AWS region that you want to store these S3 logs in?"                           "$(get_default region)"            '^[a-z]{2}-[a-z]+-[0-9]$')
DATABASE=$(   ask "Which AWS Glue Database do you want to store the logs in? (recommended: default)"            "$(get_default database_name)"     ""                         )
TABLE=$(      ask "What do you want to call the table name to store these logs?"                   "$(get_default iceberg_table_name)""                          )
BUCKET=$(     ask "What do you want to call the S3 bucket to store these logs?"           "$(get_default iceberg_s3_bucket)" '^[a-z0-9.-]{3,63}$'       )
CATALOG_ARN=$(ask "Which AWS Glue Catalog do you want to store the logs in?"                     "$(get_default iceberg_catalog_arn)"'^arn:aws:glue:[^:]+:[0-9]{12}:catalog$')
FIREHOSE=$(   ask "What do you want to call the Firehose stream?"                 "$(get_default firehose_stream_name)""                         )
LAMBDA=$(     ask "What do you want to call the Lambda function?"                 "$(get_default lambda_function_name)""                         )
CW_GROUP=$(   ask "What do you want to call the CloudWatch log group?"                 "$(get_default cloudwatch_log_group)""                         )
CW_STREAM=$(  ask "What do you want to call the CloudWatch log stream?"                "$(get_default cloudwatch_log_stream)""                        )
DEST_NAME=$(  ask "What do you want to call the Firehose destination?"            "$(get_default destination_name)"  ""                          )

# unique_accounts → JSON array
# Use previous array as commaseparated default (if present)
DEFAULT_UNIQUES=$(jq -r 'if .unique_accounts then .unique_accounts|join(",") else "" end' "$STATE_FILE")
UNIQUES_RAW=$( ask "Commaseparated unique AWS account IDs" "$DEFAULT_UNIQUES" '^([0-9]{12})(,[0-9]{12})*$' )
UNIQUES_JSON=$(jq -nc --arg csv "$UNIQUES_RAW" '$csv|split(",")')

###############################################
#  Assemble JSON and save atomically
###############################################
tmp=$(mktemp)
jq -n \
  --arg account_id            "$ACCOUNT_ID" \
  --arg region                "$REGION"     \
  --arg database_name         "$DATABASE"   \
  --arg iceberg_table_name    "$TABLE"      \
  --arg iceberg_s3_bucket     "$BUCKET"     \
  --arg iceberg_catalog_arn   "$CATALOG_ARN"\
  --arg firehose_stream_name  "$FIREHOSE"   \
  --arg lambda_function_name  "$LAMBDA"     \
  --arg cloudwatch_log_group  "$CW_GROUP"   \
  --arg cloudwatch_log_stream "$CW_STREAM"  \
  --arg destination_name      "$DEST_NAME"  \
  --argjson unique_accounts   "$UNIQUES_JSON" \
'{
    account_id:            $account_id,
    region:                $region,
    database_name:         $database_name,
    iceberg_table_name:    $iceberg_table_name,
    iceberg_s3_bucket:     $iceberg_s3_bucket,
    iceberg_catalog_arn:   $iceberg_catalog_arn,
    firehose_stream_name:  $firehose_stream_name,
    lambda_function_name:  $lambda_function_name,
    cloudwatch_log_group:  $cloudwatch_log_group,
    cloudwatch_log_stream: $cloudwatch_log_stream,
    destination_name:      $destination_name,
    unique_accounts:       $unique_accounts
}' > "$tmp"

if jq empty "$tmp" >/dev/null 2>&1; then
  mv "$tmp" "$STATE_FILE"
  echo "✅  Configuration written to $STATE_FILE"
else
  echo "❌  Generated JSON failed validation – previous state left unchanged."
  rm "$tmp"
  exit 1
fi
