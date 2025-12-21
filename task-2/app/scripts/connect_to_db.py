import psycopg2
import os  
from dotenv import load_dotenv
from scripts.logger import configure_logging

load_dotenv()

logger = configure_logging()

def get_connection():
    """
    Establish and return a connection to the PostgreSQL database.
    """

    try:
        logger.info("Connecting to PostgreSQL database...")

        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_CONTAINER"),
            port=os.getenv("HOST_PORT"),
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )

        logger.info("PostgreSQL connection established successfully.")
        return conn

    except psycopg2.Error as e:
        logger.exception("Failed to connect to PostgreSQL database: Error: {e}")
        print(e)
    
if __name__ == "__main__":
    get_connection()