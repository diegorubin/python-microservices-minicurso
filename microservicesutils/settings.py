from os.path import abspath, curdir, join
from os import environ

FRONTEND_SERVER_PORT = int(environ.get("FRONTEND_SERVER_PORT", "8888"))
USERS_SERVER_PORT = int(environ.get("USERS_SERVER_PORT", "8890"))
BOOKS_SERVER_PORT = int(environ.get("BOOKS_SERVER_PORT", "8891"))
COMMENTS_SERVER_PORT = int(environ.get("COMMENTS_SERVER_PORT", "8892"))

USERS_DATABASE_PATH = environ.get("USER_DATABASE_PATH",join(abspath(curdir), "database", "users.db"))
COMMENTS_DATABASE_PATH = environ.get("COMMENT_DATABASE_PATH",join(abspath(curdir), "database", "comments.db"))

CURRENT_APP = environ.get('CURRENT_APP', 'USERS')

LOG_PATH = environ.get("SERVICE_LOG_PATH",join(abspath(curdir), "log"))
LOG_LEVEL = environ.get("SERVICE_LOG_LEVEL", "INFO")
DEBUG = environ.get("SERVICE_DEBUG", "False") == "True"

# USERS API
USERS_AUTH_API = environ.get('USERS_HOST', 'http://localhost:8890/api/auth')
USERS_API = environ.get('USERS_HOST', 'http://localhost:8890/api/users')

# BOOKS API
BOOKS_API = environ.get('BOOKS_HOST', 'http://localhost:8891/api/books')

# COMMENTS API
COMMENTS_API = environ.get('COMMENTS_HOST', 'http://localhost:8892/api/comments')
