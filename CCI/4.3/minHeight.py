#given an increasing order sorted array, create a bin search tree
#with min height
import math

class Node:
   def __init__(self,value):
      self.left=None
      self.right=None
      self.value=value

def createMinBST(array,start,end):
   if end<start:
      return None
   mid=math.floor((start+end)/2) 
   node=Node(array[mid])
   node.left=createMinBST(array,start,mid-1)
   node.right=createMinBST(array,mid+1,end)
   return node 

if __name__=="__main__":
   array=[1,4,5,7,8,9,10,20] 
   createMinBST(array,0,len(array)-1)    
