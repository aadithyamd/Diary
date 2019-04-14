import sys 

def path_print(path, i, j):

    if i == j:
        return "A{}".format(i)
    if path[i][j] == -1:
        return "(A{} x A{})".format(i, j)
    k = path[i][j]
    l = "(" + path_print(path, i, k) + " x "
    r = path_print(path, k + 1, j) + ")"

    return l + r

# Matrix Ai has dimension p[i-1] x p[i] 
def matrix_chain_mul(p, i, j, n): 
    # create n x n matrix of 0's
    m = [[0 for x in range(n)] for x in range(n)] 
    path = [[-1 for x in range(n)] for x in range(n)] 
  
    for i in range(1, n): 
        m[i][i] = 0
   
    for chain_len in range(2, n): 
        for i in range(1, n - chain_len + 1): 
            j = i + chain_len - 1
            m[i][j] = sys.maxint 
            for k in range(i, j): 
  
                # temp = cost per scalar multiplication 
                temp = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] 
                if temp < m[i][j]: 
                    m[i][j] = temp
                    path[i][j] = k 
  
    print "Order of multiplication: ", path_print(path, 1, n - 1)

    print "Minimum number of multiplications required is ", m[1][n-1] 

print "Enter the dimentions of matrices:",
arr = map(int, raw_input().split())
n = len(arr); 
  
matrix_chain_mul(arr, 1, n-1, n) 

