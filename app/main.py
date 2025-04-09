import os
import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

dsn = os.getenv("SENTRY_DSN")
sentry_sdk.init(
    dsn=dsn,
    release=os.getenv("SENTRY_RELEASE", "unknown"),
    traces_sample_rate=1.0
)

app = FastAPI()
app.add_middleware(SentryAsgiMiddleware)

@app.get("/")
def read_root():
    return {"message": "Hello from Kubernetes on AWS!"}

@app.get("/error")
def generate_error():
    division_by_zero = 1 / 0
    return {"message": "This won't be returned"}
