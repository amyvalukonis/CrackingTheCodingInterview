#implement a fn to check if a bin tree is balanced
#balanced=no nodes subtrees differ by more than 1 
class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

   def checkHeight(self,root):
      if root is None:
         return 0 
      leftHeight=self.checkHeight(root.left) 
      if leftHeight is -1:
         return -1 
      rightHeight=self.checkHeight(root.right)
      if rightHeight is -1:
         return -1
      difference=leftHeight-rightHeight
      if abs(difference)>1:
         return -1
      else:
         return max(leftHeight,rightHeight) + 1 

   def balanced(self,root):
      if self.checkHeight(root) is -1:
         return False
      return True


if __name__=="__main__":
   node = Node(2)
   node.left=Node(1)
   node.right=Node(2) 
   node.left.left=Node(4)
   node.left.left.left=Node(5)
   result=node.balanced(node)
   print("the result is %s"%result)
