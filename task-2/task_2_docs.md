# Multi-Container Setup With Docker Compose

Completed building the backend service for MindFuel, a growing mental-wellness startup that delivers daily motivational quotes to users.

### The Python service currently:

- Fetches quotes from ZenQuotes API
- Reads subscribers from a database
- Sends personalized motivational emails daily at 7 AM
- Logs all events for monitoring

During the initial pilot, MindFuel ran the service on a few different machines but managing environments manually became painful. Different machines required different Python versions, dependency conflicts occurred frequently etc.

MindFuel has now decided to fully containerize their system using Docker, so it can be reliably deployed anywhere.

As the engineer in charge, I have been given the job to containerize the application and run it using production-like containers.

## Design a multi-container application that includes:

- Python application container
- A PostgreSQL (or MySQL) database container

### Requirements:

1. Create a compose.yml file that:

2. Defines multiple services:
    - App
    - Database
    - Maps ports for external access.
    - Mounts volumes for persistence of database data.
    - Passes environment variables securely (via .env or env_file)
    - Defines service dependencies using depends_on

3. Ensure the app container:
    - Automatically connects to the database container at startup
    - Can be rebuilt with minimal friction (docker compose up --build)

4. Ensure the DB container:
    - Uses a persistent Docker volume
    - Initializes correctly

5. Verify:
    - Running docker compose up starts the entire stack
    - Application runs without errors
    - Quotes are fetched and emails delivered successfully

## Project file Structure

task-2
├── Dockerfile
├── app
│   ├── main.py
│   └── scripts
│       ├── __init__.py
│       ├── check_db_update.py
│       ├── connect_to_db.py
│       ├── database_setup.py
│       ├── fetch_quote_from_api.py
│       ├── fetch_users.py
│       ├── logger.py
│       └── send_email.py
├── docker-compose.yaml
├── log_files
│   ├── cron_log.txt
│   └── email_service.log
├── requirements.txt
└── task_2_docs.md

## Clone the Project:

Run the following commands:

```
git clone https://github.com/kabiromohd/Docker_MindFuel_Quote_Delivery_System.git

cd Docker_MindFuel_Quote_Delivery_System/task-1
```

## Setup the Users Postgres database (This is to be done once only)

Run the following command to start the Postgres database and Pgadmin services:

```
docker-compose up postgres pgadmin
```

Once the postgres service is up, execute the ```database_setup.py```, run the following:

```
cd app/scripts/

python database_setup.py
```

Verify the users have been added to the Postgres database by accessing Pgadmin via ```http://localhost:5050```

## Start the Quote Application
Run the below docker command

```
docker-compose up app
```

This should run the the application and send the email to users.

## If the Database has been setup previously

To start the Quotes service application at any time if if the database is already setup run the following docker command:
```
docker-compose up --build
```

