#!/usr/bin/env python3
import argparse, datetime as dt
from src.extract import get_sp500_tickers, fetch_prices
from src.transform import clean_prices
from src.load import upsert_companies, upsert_prices

def main(days=90):
    start=(dt.date.today()-dt.timedelta(days=days)).isoformat()
    dfc=get_sp500_tickers(); tickers=dfc['ticker'].tolist()
    dfp=fetch_prices(tickers, start=start, interval='1d')
    upsert_companies(dfc.drop_duplicates(subset=['ticker']))
    upsert_prices(clean_prices(dfp))
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--days', type=int, default=90); a=p.parse_args(); main(a.days)
