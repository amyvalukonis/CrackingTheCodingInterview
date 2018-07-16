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

   def removeAtMiddle(self,node):
      if node is None or node.nxt is None:
         print("can't be deleted")
         return False
      nodeToCopy=node.nxt
      node.val=nodeToCopy.val
      node.nxt=nodeToCopy.nxt
      return True
         
   def size(self):
      temp=self.head
      size=0
      while temp is not None:
         print("the val is %d"%temp.val)
         size=size+1
         temp=temp.nxt
      print("size is %d"%size)

if __name__=="__main__":
   node = Node(2)
   ll=LinkedList(node) 
   ll.insertAtTail(3)
   #pointing to this node below
   ll.insertAtTail(3)
   ll.insertAtTail(4)
   ll.insertAtTail(2)
   node = ll.head.nxt.nxt
   ll.removeAtMiddle(node)
   ll.size()
