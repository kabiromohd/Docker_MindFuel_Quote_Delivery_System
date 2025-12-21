FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# Copy app files
COPY app/. /app/

# Install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8500 for the application
EXPOSE 8500

CMD ["python", "main.py"]

