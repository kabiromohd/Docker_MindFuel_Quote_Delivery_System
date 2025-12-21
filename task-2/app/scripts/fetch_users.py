import os
import pandas as pd
from dotenv import load_dotenv
from scripts.logger import configure_logging
from scripts.connect_to_db import get_connection

logger = configure_logging()

def get_active_users():
    """Fetches active users from the postgres database."""

    conn = get_connection()
    logger.info(f"Connected to Postgres database to fetch active users")

    query = """
        SELECT *
        FROM users
        WHERE subscription_status = 'active';
    """

    try:
        users = pd.read_sql_query(query, conn)
        logger.info(f"Fetched {len(users)} active users from postgres database")
        return users

    finally:
        conn.close()
        logger.info("Database connection closed")

if __name__ == "__main__":
    get_active_users()

    