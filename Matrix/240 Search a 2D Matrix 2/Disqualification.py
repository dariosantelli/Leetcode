def searchMatrix(self, matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    if not matrix:
        return False

    rows = set()
    cols = set()
    output = False

    # add code to check for 2x2 matrix

    # add out of bounds rows to set
    for i in range(m):
        if matrix[i][0] > target or matrix[i][-1] < target:
            rows.add(i)

    # add out of bounds cols to set
    for j in range(n):
        if matrix[0][j] > target or matrix[-1][j] < target:
            cols.add(j)

    for i in range(m):

        # skip row if it's out of bounds
        if i in rows:
            continue

        for j in range(n):

            # skip col if out of bounds
            if j in cols:
                continue
            else:
                if matrix[i][j] == target:
                    output = True
                    break

    return output