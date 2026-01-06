FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# Install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app/. /app/

# Expose port 8500 for the application
EXPOSE 8500

CMD ["python", "main.py"]


