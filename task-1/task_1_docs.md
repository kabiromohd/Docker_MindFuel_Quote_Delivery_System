# Containerizing MindFuel’s Quote Delivery System

Completed building the backend service for MindFuel, a growing mental-wellness startup that delivers daily motivational quotes to users.

### The Python service currently:

- Fetches quotes from ZenQuotes API
- Reads subscribers from a database
- Sends personalized motivational emails daily at 7 AM
- Logs all events for monitoring

During the initial pilot, MindFuel ran the service on a few different machines but managing environments manually became painful. Different machines required different Python versions, dependency conflicts occurred frequently etc.

MindFuel has now decided to fully containerize their system using Docker, so it can be reliably deployed anywhere.

As the engineer in charge, I have been given the job to containerize the application and run it using production-like containers.

# Building the Docker image
If you choose to rebuild the image yourself here are the instructions:

run the following commands:
```
git clone https://github.com/kabiromohd/Docker_MindFuel_Quote_Delivery_System.git

cd Docker_MindFuel_Quote_Delivery_System/task-1

docker build -t quote-delivery:latest .

```

### Using the quote image on Dockerhub
You can pull the same image from docker hub by running the below command:

see [Docker Image Url](https://hub.docker.com/repository/docker/kabiromohd/data_science/tags/quote-delivery/sha256-36df422b1506af3f7fef400a73217a0fb12b693c0575f9403dde1cd811cbc4ec)
```
docker pull kabiromohd/data_science:quote-delivery
```
### Populate the secrets
Rename the ```.env_test``` to ```.env``` and populate the relevant secrets

### Create the duckdb database for the users
Open ```scripts/database_setup.py``` and populate valid users details, names and save. Run below command to setup a duckdb database:

```
python ~/scripts/database_setup.py
```

### Run the Quote App
```
docker run -it --rm --env-file .env -v $(pwd)/data:/data -v $(pwd)/log_files:/log_files kabiromohd/data_science:quote-delivery
```

This will run the Quote App and it mounts the secrets, database volume and log files volume at run-time


