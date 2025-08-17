import os
from dotenv import load_dotenv
load_dotenv()
DB_HOST=os.getenv('DB_HOST','localhost')
DB_PORT=int(os.getenv('DB_PORT','5432'))
DB_NAME=os.getenv('DB_NAME','finance')
DB_USER=os.getenv('DB_USER','postgres')
DB_PASSWORD=os.getenv('DB_PASSWORD','postgres')
DATABASE_URL=f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
START_DATE=os.getenv('START_DATE','2015-01-01')
YF_INTERVAL=os.getenv('YF_INTERVAL','1d')
