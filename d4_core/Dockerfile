FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY d4_core ./d4_core

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]