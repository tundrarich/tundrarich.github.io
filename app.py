import sys, os, git, json
import generateSPARQL as queries
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import rdflib , pprint
from rdflib import URIRef, Graph, Namespace 
from rdflib.plugins import sparql
import rdflib.plugins.sparql as sparql
import rdflib.graph as g
from rdflib.namespace import FOAF , XSD, RDFS, NamespaceManager



DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)


freezer = Freezer(app) 


@app.route("/")
def index():
  
    return render_template('index.html')


    
print(queries.getIndustryNames())

if __name__ == "__main__":
        app.run()

