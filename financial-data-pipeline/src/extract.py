import pandas as pd, yfinance as yf
from src.utils.logging_conf import get_logger
logger=get_logger(__name__)

SEED=['AAPL','MSFT','GOOGL','AMZN','META']

def get_sp500_tickers():
    return pd.DataFrame({'ticker':SEED})

def fetch_prices(tickers, start, interval='1d'):
    df=yf.download(tickers=tickers, start=start, interval=interval, group_by='ticker', progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df=df.stack(level=0).rename_axis(index=['Date','Ticker']).reset_index()
        df=df.rename(columns={'Date':'price_date','Ticker':'ticker','Adj Close':'adj_close','Close':'close','High':'high','Low':'low','Open':'open','Volume':'volume'})
    else:
        df=df.reset_index().rename(columns={'Date':'price_date'}); df['ticker']=tickers[0]
    df['ticker']=df['ticker'].astype(str).str.replace('.','-',regex=False).str.upper()
    return df[['ticker','price_date','open','high','low','close','adj_close','volume']]
