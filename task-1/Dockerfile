FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# Copy app files
COPY app/. /app/

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

