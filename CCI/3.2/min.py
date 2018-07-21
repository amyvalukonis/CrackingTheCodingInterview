#implement a min function for stacks that operates in O(1) time

class Node:
   def __init__(self,value,minimum):
      self.value=value
      self.minimum=minimum

class Stack:
   def __init__(self):
      self.items=[] 

   def push(self, value):
      top=self.peek()
      newMin=0
      if top is None or value < top.value:
         newMin=value
      else:
         newMin=top.value
      node=Node(value,newMin)
      self.items.append(node) 

   def pop(self):
      try:
         self.items.pop() 
      except TypeError:
         print("No items in stack")

   def size(self):
      return len(self.items) 

   def isEmpty(self):
      return self.items==[] 

   def peek(self):
      if not self.isEmpty(): 
         return self.items[len(self.items)-1] 
      return None

   def findMin(self):
      if not self.isEmpty():
         topNode=self.items[self.size()-1]
         return (topNode.minimum)
      else:
         print("No items in stack")

if __name__=="__main__":
   stack = Stack() 
   minimum=stack.findMin()
