from sqlalchemy import create_engine, text
from src.config import DATABASE_URL
from src.utils.logging_conf import get_logger

def get_engine(url=None):
    eng=create_engine(url or DATABASE_URL, pool_pre_ping=True, future=True)
    with eng.connect() as c:
        c.execute(text('SELECT 1'))
    get_logger(__name__).info('Connected to database OK')
    return eng
