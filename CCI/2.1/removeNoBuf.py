import sys

#singly linked list
class Node:
   def __init__(self,val):
      self.val=val
      self.nxt=None

class LinkedList:
   def __init__(self,head=None):
      self.head=head

   #inserts value at tail of linked list
   def insertAtTail(self,data):
      node=Node(data)
      temp=self.head
      while temp.nxt is not None:
         temp=temp.nxt
      temp.nxt=node

   def removeDup(self):
      main=self.head
      while main is not None:
         val = main.val
         runner=main
         #don't want while runner!=None because runner.nxt could be None
         #and then you are accessing its value..which doesn't exist
         while runner.nxt is not None:
            if runner.nxt.val is val:
               runner.nxt=runner.nxt.nxt
            else:
               runner=runner.nxt
         main=main.nxt
         
   def size(self):
      temp=self.head
      size=0
      while temp is not None:
         size=size+1
         temp=temp.nxt
      print("size is %d"%size)

if __name__=="__main__":
   node = Node(2)
   ll=LinkedList(node) 
   ll.insertAtTail(3)
   ll.insertAtTail(3)
   ll.insertAtTail(4)
   ll.insertAtTail(2)
   ll.removeDup()
   ll.size()
