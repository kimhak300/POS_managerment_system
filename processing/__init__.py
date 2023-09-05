from flask import Flask
from processing.constant import static_folder


app = Flask(__name__, static_folder=static_folder)

from processing import routes


