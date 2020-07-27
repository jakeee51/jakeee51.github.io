import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = ""
    #SERVER_NAME = "jakemorfe.tech"
    ADMINS = []
    DEBUG = False if int(os.environ.get("FLASK_DEBUG", 0)) == 0 else True
    ENVIRONMENT = os.environ.get("FLASK_ENV")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    RUN_MODE = "dev" # "dev" -> development | "prod" -> production
