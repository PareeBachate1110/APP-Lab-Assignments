def lcs(X, Y):
    m=len(X)
    n=len(Y)
    
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]       # Create LCS table

    for i in range(m + 1):                                  # Fill the table
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(
                    lcs_table[i - 1][j],
                    lcs_table[i][j - 1]
                )

    index = lcs_table[m][n]                                 # Find the LCS string
    lcs_string = [""] * index

    i = m
    j = n

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_string)


# Example
X = "AGGTAB"
Y = "GXTXAYB"

print("Longest Common Subsequence:", lcs(X, Y))
print("Length:",len(lcs(X,Y)))