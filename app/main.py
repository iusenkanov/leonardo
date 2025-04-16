import os
import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

dsn = os.getenv("SENTRY_DSN")
sentry_sdk.init(
    dsn="https://501a7f30735cc02fcefd7878630bf1f6@o4509091708928000.ingest.us.sentry.io/4509116861972480",
    max_breadcrumbs=50,
    debug=True,
    send_default_pii=True,
    traces_sample_rate=1.0,
    release=f"myapp@{os.getenv('ARGOCD_APP_REVISION')}"
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Kubernetes on AWS!"}

@app.get("/error")
def generate_error():
    division_by_zero = 1 / 0
    return {"message": "This won't be returned"}
