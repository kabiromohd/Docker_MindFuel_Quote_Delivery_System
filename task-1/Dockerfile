FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# Copy only necessary files to leverage Docker cache
COPY app/. /app/

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]


# Build the Docker image
# docker build -t quote-delivery:latest .

# If mounting .env at runtime instead
# docker run -it --rm --env-file .env -v $(pwd)/data:/data -v $(pwd)/log_files:/log_files quote-delivery:latest
