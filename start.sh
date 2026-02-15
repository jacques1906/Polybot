#!/usr/bin/env sh
set -e

python -m pip install --upgrade pip
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# run once (dry-run)
python fastloop_trader.py --config
python fastloop_trader.py
