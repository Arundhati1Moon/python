'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Graph:
    def __init__(self,vertices):
        self.map = {} # adjacency list
        self.vertices = vertices
        for index in range(vertices):
            # initialise map with empty list
            self.map[index] = []     
            
    # Function to add an edge to graph 
    def addEdge(self, u, v):
         #Add w to v list  undirected graph
        self.map[u].append(v)
         #Add v to w list 
        self.map[v].append(u) 
        
    def print_graph(self):
        for index in range(self.vertices):
            print(index , "->", self.map[index])
        
        
g = Graph(5)
g.addEdge(1, 0) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
g.print_graph()
