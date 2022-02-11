def birthdayCakeCandles(candles):
    x = max(candles)
    y = 0
    for i in range(len(candles)):
        if candles[i] == x:
            y += 1
    return y 