import sys, os, git
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer



DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)


freezer = Freezer(app) 

@app.route("/")
def index():
    return render_template('index.html')




if __name__ == "__main__":
        app.run()

