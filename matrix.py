import math

a = [2, 3, 4, 1, 0, 0]
b = [0, 1000, 1, 100, 0, 10]
n = 2
m = 3

def display_matrix(matrix, n, m):
    rowStr = ''
    for i in range(m*n):
        rowStr += str(matrix[i])+' '
        if((i+1)%m == 0):
            print(rowStr)
            rowStr = ''

def mult_matrix(a, b, n, m):
    c = []
    y = 0
    while(y < n):
        sum = 0
        j = 0
        i = 0
        while(j < n):
            print(a[y*m+i], b[i*n+j])
            sum += a[y*m+i]*b[i*n+j]
            i+=1
            if(i < m):
                continue
            c.append(sum)
            j += 1
            sum = 0
            i = 0
        y+=1
    return c
display_matrix(mult_matrix(a, b, n, m), 2, 2)

    
    