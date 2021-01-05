  
N = 4

  
def transpose(A,B): 
  
    for i in range(N): 
        for j in range(N): 
            B[i][j] = A[j][i] 
 
A = [ [4, 7, 3, 0], 
    [3, 0, 0, 1], 
    [5, 8, 10, 2], 
    [4, 10, 8, 3]] 
   
   
B = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]  
  
transpose(A, B) 
   
print("Result matrix is") 
for i in range(N): 
    for j in range(N): 
        print(B[i][j], " ", end='') 
    print() 
      
