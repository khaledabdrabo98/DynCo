from pyld import jsonld
from rdflib import Graph
from pyshacl import validate
import json

# Read file and load json into dictionnary
with open('issues.json', 'r') as file:
    filestring = file.read()
doc = json.loads(filestring)
# print(doc)

# Load context 
with open('context.json', 'r') as file:
    filestring = file.read()
context = json.loads(filestring)
# print(context)

# Obtain RDF using dictionnary and context
rdf = jsonld.to_rdf( doc, {
    'expandContext': context,  # contexte à appliquer
    'format': 'application/n-quads', # format de sortie
})

# Export rdf to rdf.nq 
out = open('rdf.nq', 'w')
out.write(rdf)
out.close()
# print(rdf) 

# Load SHACL trace model into graph (using RDFLib) 
graph_shacl = Graph()
graph_shacl.parse('trace_model.shacl.ttl', format='ttl')
# print(graph_shacl)

# Symantic verification in RDF
r = validate(rdf,
    shacl_graph=graph_shacl,
    ont_graph=None,
    inference='rdfs',
    abort_on_first=False,
    allow_infos=True,
    allow_warnings=True,
    meta_shacl=False,
    advanced=False,
    js=False,
    data_graph_format='nquads',
    debug=False
)

conforms, results_graph, results_text = r
print(results_text)
