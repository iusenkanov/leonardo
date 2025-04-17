FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir sentry-sdk uvicorn fastapi

ARG SENTRY_RELEASE=dev
ENV SENTRY_RELEASE=$SENTRY_RELEASE

COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
