#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    a = b = scores[0]
    min_m = max_m = 0
    for i in scores[1:]:
        if i>b:
            max_m += 1
            b = i
        elif i<a:
            min_m += 1
            a = i
        
    return max_m, min_m