class Stack: 
   def __init__(self):
      self.items=[]

   def pop(self):
      return self.items.pop() 

   def push(self,item):
      self.items.append(item)

   def isEmpty(self):
      return self.items==[] 

   def peek(self):
      return self.items[len(self.items)-1]

   def size(self):
      return len(self.items) 

class Node:
   def __init__(self,value):
      self.value=value
      self.nxt=None

class LinkedList:
   def __init__(self, head=None): 
      self.head=head

   #traverse to end of list before adding
   def addToTail(self,node):
      if self.head is None:
         self.head=node
      else:
         temp=self.head
         while temp.nxt is not None:
            temp=temp.nxt
         temp.nxt=node

   def isPalindrome(self):
      stack = Stack()
      fast=self.head
      slow=self.head
      
      while fast is not None and fast.nxt is not None: 
         fast=fast.nxt.nxt
         stack.push(slow.value)
         print("slow value is %d"%slow.value)
         slow=slow.nxt
     
      #the linked list contains an odd number of nodes     
      if fast is not None:
         stack.pop() 

      while slow is not None:
         value=slow.value
         if stack.pop() != value:
            return False
         slow=slow.nxt
      return True

if __name__ == "__main__":
   node1=Node(1)
   node2=Node(2)
   node3=Node(2)
   node4=Node(1)
   ll=LinkedList(node1)
   ll.addToTail(node2)
   ll.addToTail(node3)
   ll.addToTail(node4) 
   
   boolean = ll.isPalindrome() 
   print("it is %s"%boolean) 

