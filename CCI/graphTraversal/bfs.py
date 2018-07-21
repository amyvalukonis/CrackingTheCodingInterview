from collections import defaultdict 

#FIFO
class Queue:
   def __init__(self):
      self.items=[] 

   def enqueue(self,value):
      self.items.insert(0,value)

   def dequeue(self): 
      return self.items.pop() 

   def isEmpty(self):
      return self.items==[]

class Graph:
   def __init__(self):
      self.graph = defaultdict(set) 
      
   def addEdge(self,u,v):
      self.graph[u].add(v) 

   def dfs(self,vertex,visited=None): 
      if visited is None: 
         visited=set() 
      visited.add(vertex)
      for neighbor in self.graph[vertex]-visited:
         self.dfs(neighbor,visited) 
      return visited
         
   def bfs(self,vertex):   
      queue=Queue() 
      visited=set()
      queue.enqueue(vertex)
      while not queue.isEmpty():
         v=queue.dequeue()
         for neighbor in self.graph[v]-visited:
            queue.enqueue(neighbor)
            visited.add(neighbor) 
      return visited

if __name__=="__main__":
   g = Graph() 
   g.addEdge(0, 1)
   g.addEdge(0, 2)
   g.addEdge(1, 2)
   g.addEdge(2, 0)
   g.addEdge(2, 3)
   g.addEdge(3, 3)
   path = g.dfs(0)
   pathBFS=g.bfs(0) 
   print(list(path))
   print(list(pathBFS))
