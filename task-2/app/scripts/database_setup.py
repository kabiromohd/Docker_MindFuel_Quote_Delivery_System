import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables
load_dotenv()

def get_connection_setup():
    """
    Establish and return a connection to the PostgreSQL database.
    """

    try:
        print("Connecting to PostgreSQL database...")

        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("HOST_PORT"),
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )

        print("PostgreSQL connection established successfully.")
        return conn

    except psycopg2.Error as e:
        print("Failed to connect to PostgreSQL database: Error: {e}")
        return None


def setup_database(conn):
    """
    Set up the database schema and insert sample data.
    """
    try:
        with conn.cursor() as cur:
            # Create users table
            cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                subscription_status VARCHAR(10)
                    CHECK (subscription_status IN ('active', 'inactive'))
                    DEFAULT 'active',
                email_frequency VARCHAR(10)
                    CHECK (email_frequency IN ('daily', 'weekly'))
                    DEFAULT 'daily',
                last_emailed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)

            # Insert sample data (idempotent)
            cur.execute("""
            INSERT INTO users
                (user_id, name, email, subscription_status, email_frequency)
            VALUES
                (1, 'Full Name 1', 'example_email_1@yahoo.com', 'active', 'daily'),
                (2, 'Full Name 2', 'example_email_2@gmail.com', 'active', 'weekly'),
                (3, 'Full Name 3', 'example_email_3@yahoo.com', 'inactive', 'daily'),
                (4, 'Full Name 4', 'example_email_4@gmail.com', 'active', 'weekly'),
                (5, 'Full Name 5', 'example_email_5@yahoo.com', 'active', 'daily')
            ON CONFLICT (user_id) DO NOTHING;
            """)

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise

    finally:
        conn.close()


conn = get_connection_setup()

if conn:
    setup_database(conn)
    print("Database setup completed successfully.")
else:

    print("Database setup aborted due to connection failure.")
