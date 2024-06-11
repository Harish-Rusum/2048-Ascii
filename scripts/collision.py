def collisionCalc(mat, dir):
    if dir in ["r","l"]:
        if dir == "r":
            for j in range(len(mat)):
                row = mat[j]
                for i in range(3):
                    if row[i] == row[i+1]:
                        row[i+1] = 2 * row[i]
                        row[i] = 0
                mat[j] = row
        if dir == "l":
            for j in range(len(mat)):
                row = mat[j]
                for i in range(4):
                    if row[i] == row[i-1]:
                        row[i-1] = 2 * row[i]
                        row[i] = 0
                mat[j] = row
    if dir in ["d","u"]:
        transposed = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
        if dir == "d":
            for j in range(len(transposed)):
                row = transposed[j]
                for i in range(3):
                    if row[i] == row[i+1]:
                        row[i+1] = 2 * row[i]
                        row[i] = 0
                transposed[j] = row
        if dir == "u":
            for j in range(len(transposed)):
                row = transposed[j]
                for i in range(4):
                    if row[i] == row[i-1]:
                        row[i-1] = 2 * row[i]
                        row[i] = 0
                transposed[j] = row
        mat = [[transposed[j][i] for j in range(len(transposed))] for i in range(len(transposed[0]))]
    return mat
