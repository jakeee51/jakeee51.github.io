from flask import Flask
from config import Config
import os, re

if Config.RUN_MODE == "dev":
    print(">>>", os.path.basename(__file__))

app = Flask(__name__)
app.config.from_object(Config)

from portfolio import routes

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
