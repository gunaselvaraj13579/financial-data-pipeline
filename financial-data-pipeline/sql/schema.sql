CREATE TABLE IF NOT EXISTS companies (ticker varchar(10) primary key);
CREATE TABLE IF NOT EXISTS prices_daily (ticker varchar(10), price_date date, primary key(ticker, price_date));
