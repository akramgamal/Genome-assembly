def kmer(sequences,k):
    kmers=[]
    for i in range(len(sequences)):
        for j in range(len(sequences[i])):
             if(j+(k-1)<len(sequences[i])):
                kmers.append(sequences[i][j:j+k])
    
    return kmers

def DeBruijn(sequences,k):
    kmers=kmer(sequences,k)
    nodes=[]
    edges=[]
    for i in range(len(kmers)):
        a=kmers[i][0:k-1]
        b=kmers[i][1:k]
        if a not in nodes:
            nodes.append(a)
        if b not in nodes:
            nodes.append(b)
        edges.append([a,b])
    return nodes,edges


nodes,edges=DeBruijn(["TTACGTT","CCGTTA","GTTAC","GTTCGA","CGTTC"],5)

import networkx, matplotlib.pyplot as plot 

dbGraph = networkx.DiGraph()
dbGraph.add_nodes_from(nodes) #Add the nodes to the graph
dbGraph.add_edges_from(edges) #Add the edges to the graph
networkx.draw(dbGraph, with_labels=True, node_size=1000)
plot.show()



