# matrix_A = [[n1, n2,...nc],[n3,n4,...nc],.....[nr......nc]
def matrix_transpose(matrix_A):
    rows = len(matrix_A)
    col = len(matrix_A[0])
    
    matrix_T=[]

    matrix_T = [[ matrix_A[i][j] for i in range (0,rows)] for j in range (0,col)]
             
    return(matrix_T)


#what is the benefit of if and elseif instead of multiple ifs 
def matrix_det(matrix_A):
    rows = len(matrix_A)
    col = len(matrix_A[0])

    if rows != col:
        print("Determinants are defined only for square matrices. Returning 0")
        return 0
                
    if rows > 2:
        print("can't calculate determinant for size greater than ",rows," . Returning 0")
        return 0
        
    if rows < 2:
        return (matrix_A)
        
    if rows == 2:
        return ((matrix_A[0][0] * matrix_A[1][1]) - (matrix_A[0][1] * matrix_A[1][0]))  
    
    print("unexpected error")
    return 0      
    
        
def matrix_add(matrix_A, matrix_B):
    rows_A = len(matrix_A)
    col_A = len(matrix_A[0])
    
    rows_B = len(matrix_B)
    col_B = len(matrix_B[0])
    
    if (rows_A != rows_B) or (col_A != col_B):
        print ("matrix addition can only  be performed on matrices with same number of rows and columsn, returning 0")
        return 0
    
    matrix_sum = []
    for i in range (0, rows_A):
        temp = []
        for j in range (0, col_A):
            temp.append(matrix_A[i][j] + matrix_B[i][j])
        matrix_sum.append(temp)
                
    return matrix_sum
            
            
def matrix_mult(matrix_A, matrix_B):

    rows_A = len(matrix_A)
    col_A = len(matrix_A[0])
    
    rows_B = len(matrix_B)
    col_B = len(matrix_B[0])
    
    if col_A != rows_B:
        print ("To multiply an m×n matrix by an n×p matrix, the ns must be the same, and the result is an m×p matrix. returning 0")
        return 0

    matrix_mult = []
    for i in range (0, rows_A):   
        temp = []
        for x in range (0, col_B):    
            sum = 0
            for j in range (0, col_A):    
                sum = sum + (matrix_A[i][j] * matrix_B[j][x])
            temp.append(sum)   
         
        matrix_mult.append(temp)      
                
    return matrix_mult    


#result = [[sum(a * b for a, b in zip(A_row, B_col))
#                        for B_col in zip(*B)]
#                                for A_row in A]
 
#for r in result:
#    print(r)


#inverse of a 2x2 matrix
def matrix_inverse(matrix_A):

    rows_A = len(matrix_A)
    col_A = len(matrix_A[0])
    
    if (rows_A != col_A) or (rows_A > 2):
        print ("can calc inverse here only for 2x2 matrix")
        return 0
        
    det = matrix_det(matrix_A)
    print (det)
    
    temp = matrix_A[0][0]
    matrix_A[0][0] = matrix_A[1][1] / det
    matrix_A[1][1] = temp /det
    matrix_A[0][1] = (matrix_A[0][1] * -1)/ det
    matrix_A[1][0] = (matrix_A[1][0] * -1)/ det
    
    return(matrix_A)
    
    



