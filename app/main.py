import os
import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

dsn = os.getenv("SENTRY_DSN")
sentry_sdk.init(
    dsn=dsn,
    traces_sample_rate=1.0
)

app = FastAPI()
app.add_middleware(SentryAsgiMiddleware)

@app.get("/")
def read_root():
    return {"message": "Hello from Kubernetes on AWS!"}

@app.get("/error")
def generate_error():
    try:
        1 / 0
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)  # Still send to Sentry
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal error. We've been notified."}
        )