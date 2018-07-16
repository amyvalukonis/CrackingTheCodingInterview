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
      temp=self.head
      dictionary={}
      prev=None
      while temp is not None:
         #checks if key is in the dictionary
         if temp.val in dictionary:
            prev.nxt=temp.nxt
         #else, first occurrence so add to dictionary
         else:
            dictionary[temp.val]=None
         prev=temp
         temp=temp.nxt
         
   #finds the kth element from end of list
   def kth(self, k):
      if k<0:
         return None
      temp=self.head
      #move temp forward k spaces
      for i in range(k):
         if temp is None:
            print("no valid node exists")
            return None
         temp=temp.nxt
      #could have exited for loop without reaching first error check
      #so must error check again
      if temp is None:
         print("no valid node exists")
         return None
      elementToFind=self.head
      prev=None
      while temp.nxt is not None: 
         temp=temp.nxt
         prev=elementToFind
         elementToFind=elementToFind.nxt
      print("the value found is %d"%elementToFind.val)

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
   ll.kth(2)
   ll.size()
