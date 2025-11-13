FROM python:3.11-slim

# Defineix la carpeta de treball dins del contenidor
WORKDIR /workspace/SIME

# Copia fitxers essencials
COPY requirements.txt .
COPY main.py .
COPY d4_core ./d4_core

# Instal·la dependències sense memòria cau
RUN pip install --no-cache-dir -r requirements.txt

# Assegura que el paquet d4_core sigui visible per Python
ENV PYTHONPATH="${PYTHONPATH}:/workspace/SIME/d4_core"

# Executa el sistema principal
CMD ["python", "main.py"]