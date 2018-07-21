
class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

   def printInorder(self,root):
      result=[]
      if root:
         result=self.printInorder(root.left)
         result.append(root.value) 
         result=result+self.printInorder(root.right) 
      return result

   def printPreorder(self,root):
      result=[]
      if root:
         result.append(root.value)
         result=result+self.printPreorder(root.left)
         result=result+self.printPreorder(root.right)
      return result

   def printPostorder(self,root):
      result=[]
      if root:
         result=self.printPostorder(root.left)
         result=result+self.printPostorder(root.right)
         result.append(root.value) 
      return result

if __name__=="__main__":
   root=Node(1) 
   root.left=Node(2)
   root.right=Node(3)
   root.left.left=Node(4)
   root.right.right=Node(5)
   result=root.printInorder(root)
   result2=root.printPreorder(root)
   result3=root.printPostorder(root)
   print("inorder traversal: %s"%result)
   print("prorder traversal: %s"%result2)
   print("postorder traversal: %s"%result3)
