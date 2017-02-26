from os.path import abspath, curdir, join
from os import environ

FRONTEND_SERVER_PORT = int(environ.get("FRONTEND_SERVER_PORT", "8888"))
LOG_PATH = environ.get("SERVICE_LOG_PATH",join(abspath(curdir), "log"))
LOG_LEVEL = environ.get("SERVICE_LOG_LEVEL", "INFO")
DEBUG = environ.get("SERVICE_DEBUG", "False") == "True"

