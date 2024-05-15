import graphviz # installeres med pip3 install graphviz
import pydot # installeres med "pip install pydot"
import os
from IPython.display import Image, display # måtte installeres med "pip install ipython"
'''
# klarer ikke installere diagrams
from diagrams import Diagram, Cluster, Edge
from diagrams.digitalocean.compute import Droplet
from diagrams.digitalocean.database import DbaasPrimary
from diagrams.elastic.elasticsearch import Logstash
'''



from graphviz import Digraph

dot = Digraph()
dot.node('a')
dot.node('b')
dot.edge('a','b')

dot.render("sample.png")


'''
# Dette er et eksempel
# create the object
dot = graphviz.Digraph('ex', comment='EX', format='png')

# add nodes
dot.node('db1', 'input A', {'color': 'aquamarine', 'style': 'filled'})
dot.node('db2', 'input B', {'color': 'aquamarine', 'style': 'filled'})
dot.node('db3', 'input C', {'color': 'aquamarine', 'style': 'filled'})

dot.node('B', 'transformation', shape='box')

dot.node('C', 'output', shape='cylinder', style='filled', fillcolor='darksalmon')

# add egdes
for n in ['db1', 'db2', 'db3']:
    dot.edge(n, 'B')

dot.edge('B', 'C')

print(dot.source)

#doctest_mark_exe()
#display_png()

dot.render(directory='doctest-output.png', view=True)  
graphviz.render('dot', 'png').replace('\\', '/')
dot

# Create image of folder tree
#im = Image(dot.create_jpeg())
# DIsplay
#display(im)
#dot.write_jpeg('output/test.jpeg')
'''




'''
# Dette er et annet eksempel
dot = graphviz.Digraph(comment='EX2')
dot.attr(newrank='true') # "needed for aligning clusters" hva nå enn det betyr

# style definitions
input_style = {'color': 'plum', 'style': 'filled'}
marker_style = {'shape': 'box', 'style': 'filled', 'fillcolor': 'lightsalmon'}
meanhood_style = {'shape': 'box', 'color': 'skyblue', 'style': 'filled'}
marker_cluster_style = {**marker_style, 'fillcolor': 'F2A48188'}
tls_style = {'shape': 'doubleoctagon', 'color': 'mediumseagreen', 'style': 'filled'}

# input data
dot.node('sig', 'Signals/ Reference', input_style)
dot.node('sig_old', 'Legacy signals', input_style)
dot.node('geo', 'Geometry', input_style)
dot.node('aux', 'Auxiliary info', input_style)

dot
'''


