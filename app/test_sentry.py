import sentry_sdk

sentry_sdk.init(
    dsn="https://501a7f30735cc02fcefd7878630bf1f6@o4509091708928000.ingest.us.sentry.io/4509116861972480",
    debug=True
)

try:
    1 / 0
except ZeroDivisionError as e:
    sentry_sdk.capture_exception(e)
