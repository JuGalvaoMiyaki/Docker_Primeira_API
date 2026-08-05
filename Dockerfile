
FROM python:3.11-slim-buster

# Instalar dependências como root
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    && rm -rf /var/lib/apt/lists/*

# Criar usuário com diretório home -
RUN useradd -m -s /bin/bash appuser

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser . /app
USER appuser

ENV FLASK_APP=app.py

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request, sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:5000/').getcode() == 200 else 1)"

CMD ["python", "app.py"]