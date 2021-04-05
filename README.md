# Stock and Bitcoin Portfolio Management
Documentation is work in progress...

## A TD Ameritrade account is required.

# Quick Start
1. Install package requirements from "requirements.txt"
2. Create a config file (sample provided) config.json, fill in the "API_KEY" vars.
3. Create portfolio JSON files (samples provided) named <portfolio>.json.  For example "webull.json".
   Entries in this file is: Portfolio, Symbol, Number of Shares, Cost.
4. Create a copy of the .env_sample to .env and edit to suit.
5. Run the authentication for the first time: ./stocks.py -a

# Basic Use Commands
- Help: ./stocks.py -h
- Stats: ./stocks.py -s
- Portfolio View: ./stocks.py -p <portfolio>
- All Portfolios: ./stocks.py -a all

