import sys, os
from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)


FREEZER_BASE_URL = "http://localhost/tundrarich.github.io"

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

pages = FlatPages(app)
freezer = Freezer(app)

@app.route("/")
def index():
    return "Testing Github"

@app.route("/<path:path>/")
def page(path):
    return pages.get_or_404(path).html

if __name__ == "__main__":
    freezer.freeze()

