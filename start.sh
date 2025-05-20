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

# ── 5. Refuse to overwrite an existing file ───────────────────────────────────
if [[ -e $filepath ]]; then
  echo "⚠️  $filepath already exists — aborting." >&2
  exit 1
fi

# ── 6. Write a minimal Python stub ────────────────────────────────────────────
cat <<PY >"$filepath"
\"\"\"Auto-generated on $(date '+%A, %B %d, %Y').\"\"\"

def main() -> None:
    print("Hello from ${filename}")

if __name__ == "__main__":
    main()
PY

echo "✅  Created $filepath"
code "$filepath"
