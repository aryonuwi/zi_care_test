FROM python:3.10.6

WORKDIR /app
RUN pip3 install --upgrade pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

RUN mkdir -p /app/migrations
COPY alembic.ini /alembic.ini
COPY alembic /alembic
COPY scripts /app/scripts

RUN chmod +x /app/migrate.sh

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
