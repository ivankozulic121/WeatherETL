from dotenv import load_dotenv
from sqlalchemy import create_engine
from transform import mergedDF
import logging
import os

load_dotenv()

logging.basicConfig(
    level=logging.INFO,   # minimum level to show
    format="%(asctime)s [%(levelname)s] %(message)s"
)

DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "secret_password")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "mydatabase")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#DB_URL = f"postgresql+psycopg2://postgres:arohadrix@localhost:5432/weather_db"

def load_data_to_db():
    try:
        engine = create_engine(DATABASE_URL)
        mergedDF.to_sql('weather_db', engine, index=False, if_exists='replace')
        logging.info("DataFrame successfully uploaded to SQL database")

    except Exception as e:
        logging.error(f"Failed to upload DataFrame to SQL: {e}")

load_data_to_db()