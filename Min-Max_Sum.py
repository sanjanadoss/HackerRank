def miniMaxSum(arr):

    x = sum(arr)
    minValue = x - max(arr)
    maxValue = x - min(arr)

    print(minValue, maxValue)