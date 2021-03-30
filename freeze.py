import sys, os, git
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from app import app

repository = git.Repo('.', search_parent_directories=True)
app.config['FREEZER_BASE_URL'] = "http://localhost/tundrarich.github.io"
app.config['FREEZER_DESTINATION'] = repository.working_tree_dir
app.config['FREEZER_REMOVE_EXTRA_FILES']  = False
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'


freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    
freezer = Freezer(app)
