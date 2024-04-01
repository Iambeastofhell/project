n  = int(input('Enter the number of the rows or columns you want : '))
matrix = [[2,0,0,0],[0,0,3,0],[0,1,0,0],[0,0,0,1]]
matrix = []
for i in range(n*n):
    i = (input(f"Enter the whole row{i+1}: "))
    i = i.split()
    for j in range(len(i)):
        i[j] = int(i[j])
    matrix.append(i)
   
print('Unsolved Sudoku: ') 
for i in matrix:
    for j in i:
        print(j,end=' ')
    print()


def giveMatrix(matrix, x, y, n):
    matrix_list = []

    for i in range(x, x + n):
        row = []
        for j in range(y, y + n):
        
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                row.append(matrix[i][j])
        matrix_list.append(row)
    return matrix_list


def makeSmallMatrix(matrix,x):
    small_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(i%x == 0 and j%x == 0):
                small_matrix.append(giveMatrix(matrix,i,j,x))
    return small_matrix

smaller_matrix = makeSmallMatrix(matrix,n)

def row_col(matrix,x,y):
    empty_list = []
    for k in range(len(matrix)):
        empty_list.append(matrix[k][y])
    for k in range(len(matrix)):
        empty_list.append(matrix[x][k])
    a = matrix[x][y]
    empty_list.remove(a)

    return empty_list


def giveSmallerMatrixForCoord(matrix,x,y):    
    x = x-x%n
    y = y//n
    ma  = makeSmallMatrix(matrix,n)
    square_matrix = ma[x+y]
    lists = []
    for i in square_matrix:
        for j in i:
            lists.append(j)
    return lists

check_set = {i+1 for i in range(n*n)}

def changeMatrix(matrix):    

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == 0):
                if(len(check_set-set(giveSmallerMatrixForCoord(matrix,i,j))-set(row_col(matrix,i,j))) == 1):
                    
                    matrix[i][j] = (check_set-set(giveSmallerMatrixForCoord(matrix,i,j))-set(row_col(matrix,i,j))).pop()

    return matrix

def checkSudokuSolved():
    matrixx = changeMatrix(matrix)

    isSolved = sum(bool(j) for i in matrixx for j in i) == n**4
    if not isSolved:
        return checkSudokuSolved()
    else:
        return matrixx



ans_matrix = checkSudokuSolved()
print('Solved Sudoku is : ')
for i in ans_matrix:
    for j in i:
        print(j,end=' ')
    print()
