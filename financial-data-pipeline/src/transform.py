import pandas as pd

def clean_prices(df: pd.DataFrame) -> pd.DataFrame:
    df=df.copy(); df['price_date']=pd.to_datetime(df['price_date']).dt.date
    for c in ['open','high','low','close','adj_close','volume']:
        df[c]=pd.to_numeric(df[c], errors='coerce')
    df=df.dropna(subset=['ticker','price_date','close'])
    df=df.drop_duplicates(subset=['ticker','price_date'], keep='last')
    return df
