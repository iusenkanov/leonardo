import os
import sentry_sdk
from fastapi import FastAPI

dsn = os.getenv("SENTRY_DSN")
sentry_sdk.init(
    dsn=dsn,
    traces_sample_rate=1.0
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Kubernetes on AWS!"}

@app.get("/error")
def generate_error():
    division_by_zero = 1 / 0
    return {"message": "This won't be returned"}
