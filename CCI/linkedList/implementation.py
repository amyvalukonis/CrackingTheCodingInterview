import sys

class Node:
   def __init__(self,val):
      self.val=val 
      self.nxt=None
      self.prev=None 

class LinkedList: 
   #initalizes a linked list, default head value = None 
   def __init__(self,head=None): 
      self.head=head

   #inserts a value at the head of the linked list
   def insert(self,data): 
      newNode = Node(data)
      if self.head==None:
         self.head=newNode
      else:
         newNode.nxt=self.head
         self.head.prev=newNode
         self.head=newNode

   #checks if a particular value is in the linked list
   def search(self, data): 
      temp = self.head
      while temp is not None: 
         if temp.val==data:
            print(True)
            return 
         temp=temp.nxt
      print(False)
      return 

   #inserts value at tail of linked list
   def insertAtTail(self,data):
      node=Node(data)
      temp=self.head
      while temp.nxt is not None: 
         temp=temp.nxt
      temp.nxt=node
      node.prev=temp

   #prints tail of the linked list
   def printLast(self):
      temp=self.head
      while temp.nxt is not None:
         temp=temp.nxt
      print(temp.val)

   #deletes a value from the linked list assuming it is in the list
   def deleteVal(self,val):
      temp=self.head
      while temp is not None:
         if temp.val is val:
            newNext=temp.nxt
            newPrev=temp.prev
            #need to check if accessing None type Node
            if newNext is not None:
               temp.nxt.prev=temp.prev
            if newPrev is not None:
               temp.prev.nxt=temp.nxt
            return 
         temp=temp.nxt
      return 
 
   def printSize(self):
      temp=self.head
      size=0
      while temp.nxt is not None:
         temp=temp.nxt
         size=size+1

   def retrieveHead(self):
      return self.head.val


if __name__=="__main__":
   node = Node(1)
   ll = LinkedList(node)
   ll.insertAtTail(2) 
   ll.insertAtTail(3) 
   ll.deleteVal(2)
   ll.printLast()


