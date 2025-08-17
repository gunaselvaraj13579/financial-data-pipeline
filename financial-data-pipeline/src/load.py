from sqlalchemy import text
from src.utils.db import get_engine

def upsert_companies(df):
    eng=get_engine(); rec=df.fillna('').to_dict('records')
    sql=text('INSERT INTO companies (ticker) VALUES (:ticker) ON CONFLICT (ticker) DO NOTHING')
    with eng.begin() as c: c.execute(sql, rec)

def upsert_prices(df):
    eng=get_engine(); rec=df.to_dict('records')
    sql=text('INSERT INTO prices_daily (ticker, price_date) VALUES (:ticker, :price_date) ON CONFLICT (ticker, price_date) DO NOTHING')
    with eng.begin() as c: c.execute(sql, rec)
