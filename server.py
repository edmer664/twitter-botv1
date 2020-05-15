from os import environ
from flask import Flask

app.run(host= '0.0.0.0', port=environ.get('PORT'))
app = Flask(__name__)
app.run(environ.get('PORT'))
