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
    while(y < m):
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

def add_matrix(a, b):
    c = []
    for i in range(len(a)):
            c.append(a[i]+b[i])
    return c

def sub_matrix(a, b):
    c = []
    for i in range(len(a)):
            c.append(a[i]-b[i])
    return c

def transpose(a, n, m):
    b = []
    for i in range(m):
            for j in range(n):
               b.append(a[i+j*m])
    return b 

def det(a):
     return a[0]*a[3]-a[1]*a[2]


def systems_of_linear_equation(co_matrix, result_matrix):
    d = det(co_matrix)
    inverse_matrix = [co_matrix[3]/d, -co_matrix[1]/d, -co_matrix[2]/d, co_matrix[0]/d]
    display_matrix(inverse_matrix, 2, 2)
    final_matrix = mult_matrix(inverse_matrix, result_matrix, 1, 2)
    return final_matrix

n1 = [1, 3, 1, 1, 0, 0]
n2 = [0, 0, 5, 7, 5, 0]
n3 = [1, 2, 3, 0, -6, 7]
n4 = [4, 7, 2, 6]
# print(det(n4))
# display_matrix(mult_matrix(a, b, n, m), 2, 2)
# display_matrix(add_matrix(n1, n2), 2, 3)
# display_matrix(transpose(n3, 2, 3), 3, 2)

display_matrix(systems_of_linear_equation([2, 7, 5, -4], [34, -1]), 2, 1)