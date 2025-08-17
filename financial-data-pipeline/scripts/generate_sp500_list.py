#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from src.extract import get_sp500_tickers
out=Path('data'); out.mkdir(parents=True, exist_ok=True)
df=get_sp500_tickers(); df.to_csv(out/'sp500_tickers.csv', index=False)
print('saved', len(df))
