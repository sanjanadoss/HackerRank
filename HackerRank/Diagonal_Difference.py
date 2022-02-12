def diagonalDifference(arr):
    # Write your code here
    d1 = sum([arr[x][x] for x in range(n)]) 
    d2 = sum([arr[x][n-1-x] for x in range (n)])
    return(abs(d1-d2))
