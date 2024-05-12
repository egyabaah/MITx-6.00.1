def searchMatrix(matrix, target):
    c = [0, -1]
    while c[0] < len(matrix) and c[1] >= -(len(matrix[c[0]])):
        if target > matrix[c[0]][c[1]]:
            c[0] += 1
        elif target < matrix[c[0]][c[1]]:
            c[1] -= 1
        else:
            return True
    print(c[0])
    return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 7, 8, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]

matrix1 = [[-5]]

print(searchMatrix(matrix1, -5))
print(-5 in matrix1)
