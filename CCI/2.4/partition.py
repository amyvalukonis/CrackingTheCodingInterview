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

   def partition(self, value):
      #create two linked lists with head values set to None
      smallerList=LinkedList() 
      biggerList=LinkedList() 
      #the head of the calling linked list (the one to partition) 
      temp=self.head 
      while temp is not None:
         nextNode = temp.nxt 
         if temp.val < value: 
               temp.nxt=smallerList.head
               smallerList.head=temp 
         else:
               temp.nxt=biggerList.head
               biggerList.head=temp
         temp=nextNode

      #if nothing in smaller list, no need to concatenate 
      if smallerList.head is None:
         return biggerList

      #else, concatenate bigger list to smaller list
      else:
         temp=smallerList.head
         prev=temp
         while temp is not None:
            prev=temp
            temp=temp.nxt
         prev.nxt = biggerList.head
         return smallerList
            
         
   def size(self):
      temp=self.head
      size=0
      while temp is not None:
         print("val is %d"%temp.val)
         size=size+1
         temp=temp.nxt
      print("size is %d"%size)

if __name__=="__main__":
   node = Node(2)
   ll=LinkedList(node) 
   ll.insertAtTail(3)
   #pointing to this node below
   ll.insertAtTail(1)
   ll.insertAtTail(4)
   ll.insertAtTail(2)
   newList=ll.partition(2) 
   newList.size()
