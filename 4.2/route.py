from collections import defaultdict

class Graph:
   def __init__(self):
      self.graph=defaultdict(set) 

   #directed graph since only add vertex to one list
   def addEdge(self,u,v):
      self.graph[u].add(v)

   def route(self,start,end,visited=None):
      if visited is None:
         visited=set()
      visited.add(start)
      for neighbor in self.graph[start]-visited:
         if neighbor is end:
            return True
         self.route(neighbor,end,visited)
      return False 

if __name__=="__main__":
   g = Graph() 
   g.addEdge(0, 1)
   g.addEdge(0, 2)
   g.addEdge(1, 2)
   g.addEdge(2, 0)
   g.addEdge(2, 3)
   g.addEdge(3, 3)
   result=g.route(0,3)
   print(result)
