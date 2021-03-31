import rdflib , pprint, os, json, csv
from rdflib import URIRef, Graph, Namespace, BNode
from rdflib.plugins import sparql
import rdflib.plugins.sparql as sparql
import rdflib.graph as g
from rdflib.namespace import FOAF , XSD, RDFS, NamespaceManager

g = Graph()


cwd = os.getcwd()

def load_file(filename):
    current_directory = os.getcwd()
    path = 'C:\\Users\\jayba\\OneDrive\\Documents\\GitHub\\Open Data 1\\turtleFiles\\{}.ttl'.format(filename)
    g.load(path, format='turtle')


#g.parse('C:\\Users\\jayba\\OneDrive\\Documents\\GitHub\\tundrarich.github.io\\ontology\\bics.ttl', format='turtle')
BICS = Namespace('https://github.com/tundrarich/tundrarich.github.io/blob/main/ontology/bics.ttl')
g.bind("bics", BICS)

g.load('C:\\Users\\jayba\\OneDrive\\Documents\\GitHub\\Open Data 1\\turtleFiles\\Sample Size Industry.ttl', format='turtle')

load_file('Sample Size Industry')
load_file('Sample Size Workforce')
load_file('Responses Industry Numbers')
load_file('Responses Industry Proportion')
load_file('Responses Workforce Numbers')
load_file('Responses Workforce Proportion')
load_file('Trading Status Industry')
load_file('Trading Status Workforce')
load_file('Trading Status Country')
load_file('Applied Initiatives Industry')
load_file('Applied Initiatives Workforce')
load_file('Applied Initiatives Country')
load_file('Received Initiatives Industry')
load_file('Received Initiatives Workforce')
load_file('Future Initiatives Industry')
load_file('Future Initiatives Workforce')

def getIndustryNames():
    query = sparql.prepareQuery(
    """SELECT DISTINCT ?name
    WHERE { ?a bics:ContainedIndustry ?s .
    ?s rdfs:label ?name .
    
    }""", 
    initNs = {"bics": BICS, "rdfs": RDFS, "xsd": XSD})
    
    data = []
    for row in g.query(query):
      value = str(row.asdict()['name'].toPython())
      data.append(value)
      
    return data

def getIndustryTotalSent():
    query = sparql.prepareQuery(
    """SELECT ?name ?numberSent ?numberReceived ?percentageReceived
    WHERE {
    ?workforce rdfs:label "Total"^^xsd:string .
    
    ?workforce bics:hasWorkforceNumberSent ?numberSent .
    
    ?workforce bics:ContainedIndustry ?industry .
    ?industry rdfs:label ?name .
    
    }
    ORDER BY ASC(?industry)
    """,
    initNs = {"bics": BICS, "rdfs": RDFS, "xsd": XSD})
    
    names = []
    numbersSent = []
      
    for row in g.query(query):
      name = str(row.asdict()['name'].toPython())
      numberSent = (row.asdict()['numberSent'].toPython())
      
      names.append(name)
      numbersSent.append(numberSent)
     
    return names, numbersSent

def getIndustryTotalReceived():
    query = sparql.prepareQuery(
    """SELECT ?name ?numberSent ?numberReceived ?percentageReceived
    WHERE {
    ?workforce rdfs:label "Total"^^xsd:string .
    
    ?workforce bics:hasWorkforceNumberReceived ?numberReceived .
    ?workforce bics:hasWorkforcePercentageReceived ?percentageReceived .
    
    ?workforce bics:ContainedIndustry ?industry .
    ?industry rdfs:label ?name .
    
    }
    ORDER BY ASC(?industry)
    """,
    initNs = {"bics": BICS, "rdfs": RDFS, "xsd": XSD})
    
    names = []
    numbersReceived = []
    percentagesReceived = []
      
    for row in g.query(query):
      numberReceived = (row.asdict()['numberReceived'].toPython())
      percentageReceived = (row.asdict()['percentageReceived'].toPython())
      name = str(row.asdict()['name'].toPython())

      names.append(name)
      numbersReceived.append(numberReceived)
      percentagesReceived.append(percentageReceived)
      
    return names, numbersReceived, percentagesReceived

namesSent, numbersSent = getIndustryTotalSent() 
namesReceived, numbersReceived, percentagesReceived = getIndustryTotalReceived() 

numbersReceivedNew = [None] * len(namesSent)




for i in range(len(namesSent)):    
    if(namesSent[i] in namesReceived):             
        index = namesReceived.index(namesSent[i])
        numbersReceivedNew[i] = numbersReceived[index]
    else:
        numbersReceivedNew[i] = 0 
    i += 1


fullList = []
for i in range(len(namesSent)):
    fullList.append([str(namesSent[i]), numbersSent[i], numbersReceivedNew[i]])


with open('CSVfiles/industriesTotal.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(["group", "Sent", "Received"])
    for i in range(len(fullList)):
        writer.writerow(fullList[i])
        
  