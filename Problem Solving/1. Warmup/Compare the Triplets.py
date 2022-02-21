
def compareTriplets(a, b):

    c = [0]*2
    for i in range(0,3):
        if a[i] > b[i]:
            c[0] += 1
        if a[i] < b[i]:
            c[1] += 1
        else:
            c[0] += 0
            c[1] += 0
    return c
