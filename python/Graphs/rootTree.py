class Node:
    def __init__(self,id,parent,children):
        self.id = id
        self.parent = parent
        self.children = children

def rootTree(graph,rootId=0):
    root = Node(rootId,None,[])
    return buildTree(graph,root,None)

def buildTree(graph,node,parent):
    for childId in graph[node.id]:
        if parent!=None and childId==parent.id:
            continue
        child = Node(childId,node,[])
        node.children.append(child)
        buildTree(graph,child,node)
    return node