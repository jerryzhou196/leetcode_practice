#!/usr/bin/env bash
# make_daily_py.sh — create a python file named like friday_may_16th_2025.py

set -euo pipefail

# ── 1. Pull today’s date components ────────────────────────────────────────────
weekday=$(date '+%A' | tr '[:upper:]' '[:lower:]')   # friday
month=$(date '+%B'  | tr '[:upper:]' '[:lower:]')    # may
day=$(date '+%d')                                    # 16 (zero-padded)
year=$(date '+%Y')                                   # 2025

# Strip any leading zero from the day
day_num=${day#0}

# ── 2. Choose the correct ordinal suffix ──────────────────────────────────────
case "$day_num" in
  1|21|31) suffix="st" ;;
  2|22)    suffix="nd" ;;
  3|23)    suffix="rd" ;;
  *)       suffix="th" ;;
esac

# ── 3. Assemble the filename ──────────────────────────────────────────────────
filename="${weekday}_${month}_${day_num}${suffix}_${year}.py"

# ── 4. Refuse to overwrite an existing file ───────────────────────────────────
if [[ -e $filename ]]; then
  echo "⚠️  $filename already exists — aborting." >&2
  exit 1
fi

# ── 5. Write a minimal Python stub ────────────────────────────────────────────
cat <<PY >"$filename"
\"\"\"Auto-generated on $(date '+%A, %B %d, %Y').\"\"\"

def main() -> None:
    print("Hello from ${filename}")

if __name__ == "__main__":
    main()
PY

echo "✅  Created $filename"

code $filename

