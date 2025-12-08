FROM python:3.11-slim

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock /app/
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root

COPY ./src /app/src
COPY ./.env /app/.env

ENV PYTHONPATH=/app

EXPOSE 8001

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]
