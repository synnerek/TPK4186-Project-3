import graphviz
from Task import Task


g = graphviz.Digraph(filename='pertChart.gv')

activity = []
description = []
# noe annet?
#colors = ["black", "skyblue", "mistyrose", "skyblue", "skyblue", "mistyrose", "mistyrose", "mistyrose"]

for i in range(len(Task)):
    activity.append(Task.activity)
    description.append(Task.description)
    

for name, position, color in zip(activity, description):
    if name== "A":
        g.node(name, position, color = color)
    else:
        g.node(name, position, style = "filled", color = color)

#Specify edges
g.edge("A","B"); g.edge("A","C")   #CEO to Team Leads
g.edge("B","D"); g.edge("B","E")   #Team A relationship
g.edge("C","F"); g.edge("C","G"); g.edge("C","H")   #Team B relationship
    
g