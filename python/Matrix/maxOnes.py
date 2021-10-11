'''
Problem statement: Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.
'''

def rowWithMaxOnes(matrix):
    n = len(matrix)
    m = len(matrix[0])

    result = -1
    j = m - 1
    
    for i in range(n):
        flag = False
        while(j>=0 and matrix[i][j]==1):
            flag = True
            j -= 1
        if flag == True :
            result = i

    return result
        
# test code
a = [[0,0,0,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
print(rowWithMaxOnes(a))