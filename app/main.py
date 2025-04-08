import os
dsn = os.getenv("SENTRY_DSN")
sentry_sdk.init(
    dsn=dsn,
    traces_sample_rate=1.0
)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Kubernetes on AWS!"}
