FROM python:3.11-slim
RUN pip install --no-cache-dir -U pip
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
