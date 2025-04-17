import os
import sentry_sdk
from fastapi import FastAPI

# Get Sentry DSN and release version from environment
dsn = os.getenv("SENTRY_DSN")
release = os.getenv("SENTRY_RELEASE", "dev")  # fallback to 'dev' if not set

# Initialize Sentry
sentry_sdk.init(
    dsn=dsn,  # Use env var for security and flexibility
    release=release,  # Set release version for better tracking
    max_breadcrumbs=50,
    debug=True,
    send_default_pii=True,
    traces_sample_rate=1.0,
)

# FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Kubernetes on AWS!"}

@app.get("/error")
def generate_error():
    # This will be captured by Sentry
    division_by_zero = 1 / 0
    return {"message": "This won't be returned"}
