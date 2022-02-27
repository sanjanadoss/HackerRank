#https://www.hackerrank.com/challenges/the-hurdle-race/problem

def hurdleRace(k, height):
    key = max(height)
    if k>key:
        return 0
    else:
        return key-k