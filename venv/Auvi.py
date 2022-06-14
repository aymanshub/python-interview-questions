matrix = [
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
          ]

def are_nieghbours_ones(i, j, matrix, rows, columns):

    i, j-1
    i-1, j-1
    i-1, j
    i-1, j+1
    i, j+1
    i+1, j+1
    i+1, j
    i+1, j-1

    indexer = [-1, 0, 1]
    for m in indexer:
        for n in indexer:
            if matrix[i+m][j+n] != 1 and (m !=0 and n!=0):
                return False
            else:
                continue

    return True



def manipulate(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns):
           ## matrix[i,j]
           if not are_nieghbours_ones(i,j, matrix) and matrix[i][j]==0:
                matrix[i][j] = matrix[i][j] + 1

