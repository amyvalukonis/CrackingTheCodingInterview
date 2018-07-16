import sys

if __name__=="__main__": 
   matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,0]] 
   #matrix=[[0,0],[0,1]]
   rows=[0]*len(matrix) #lists to keep track of if already assigned zero
   cols=[0]*len(matrix[0])
   for row in range (0,len(matrix)): 
      for col in range(0,(len(matrix[row]))):
         if matrix[row][col] is 0:
            rows[row]=1
            cols[col]=1
   for row in range(0,len(matrix)):
      for col in range(0,(len(matrix[row]))):
         if rows[row] or cols[col]:
            matrix[row][col]=0
   print(matrix) 

