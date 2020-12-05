def flipAndInvertImage(self, A):
    for i in range(len(A)):  # for each sublist
        list.reverse(A[i])

    for i in range(len(A)):  # sublist
        for j in range(len(A[i])):  # inside sublists
            if A[i][j] == 1:
                A[i][j] = 0
            else:
                A[i][j] = 1

    return A