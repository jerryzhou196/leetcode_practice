#!/usr/bin/env bash
# make_daily_py.sh — create a daily directory (MM-DD-YYYY) and a Python stub
set -euo pipefail

# ── 1. Pull today’s date components ────────────────────────────────────────────
weekday=$(date '+%A' | tr '[:upper:]' '[:lower:]')   # monday
month=$(date '+%B' | tr '[:upper:]' '[:lower:]')     # may
day=$(date '+%d')                                    # 19 (zero-padded)
year=$(date '+%Y')                                   # 2025
# Purely-numeric directory name (MM-DD-YYYY)
daily_dir=$(date '+%m-%d-%Y')                        # 05-19-2025
current_date_for_commit=$(date '+%Y-%m-%d')         # For commit message

# ── 2. Choose the correct ordinal suffix ──────────────────────────────────────
day_num=${day#0}   # strip leading zero
case "$day_num" in
  1|21|31) suffix="st" ;;
  2|22)    suffix="nd" ;;
  3|23)    suffix="rd" ;;
  *)       suffix="th" ;;
esac

# ── 3. Assemble paths ─────────────────────────────────────────────────────────
filename="${weekday}_${month}_${day_num}${suffix}_${year}.py"
filepath="$daily_dir/$filename"

# ── 4. Create the directory (safe if it already exists) ───────────────────────
mkdir -p "$daily_dir"

# ── 5. If today's file already exists, open the most recently created .py ────
if [[ -e $filepath ]]; then
  echo "⚠️  $filepath already exists — opening most recently created file." >&2
  most_recent=$(find . -type f -name '*.py' -not -path './.*' -print0 \
    | xargs -0 stat -f '%B %N' \
    | sort -rn \
    | head -n 1 \
    | cut -d' ' -f2-)
  if [[ -n $most_recent ]] && command -v nvim &> /dev/null; then
    nvim "$most_recent"
  elif [[ -n $most_recent ]]; then
    echo "ℹ️  'nvim' command not found. Most recent file: $most_recent"
  else
    echo "ℹ️  No .py files found."
  fi
  exit 0
fi

# ── 6. Write a minimal Python stub ────────────────────────────────────────────
cat <<PY >"$filepath"
"""Auto-generated on $(date '+%A, %B %d, %Y')."""

def main() -> None:
    print("Hello from ${filename}")

if __name__ == "__main__":
    main()
PY

echo "✅  Created $filepath"

# ── 7. Git add and commit with a random message ───────────────────────────────
# Array of random commit phrases
commit_phrases=(
    "🚀 Initial commit for"
    "✨ Added solution stub for"
    "🎉 Began work on"
    "💡 Drafted initial file for"
    "🌟 New LeetCode problem:"
    "🎯 Starting point for"
    "🥳 Kicking off"
)

# Get a random index
num_phrases=${#commit_phrases[@]}
random_index=$((RANDOM % num_phrases))

# Select a random phrase
random_phrase="${commit_phrases[$random_index]}"

# Construct the commit message
commit_message="${random_phrase} ${filename} on ${current_date_for_commit}"

# Add all changes in the current directory
git add .

# Commit the changes
git commit -m "$commit_message"

echo "💾  Committed with message: $commit_message"

# ── 8. Open the file (optional) ───────────────────────────────────────────────
if command -v nvim &> /dev/null; then
    nvim "$filepath"
else
    echo "ℹ️  'nvim' command not found. Skipping opening the file in nvim."
fi
