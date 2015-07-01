from flask import Flask, url_for
import os

demere = Flask(__name__)
demere.secret_key = 'secret key'
# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
demere.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

from demere import views
