import sys, os, git
from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)

repo = git.Repo('.', search_parent_directories=True)

FREEZER_BASE_URL = "http://localhost/tundrarich.github.io"
FREEZER_DESTINATION = repo.working_tree_dir
FREEZER_REMOVE_EXTRA_FILES = False

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
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)

