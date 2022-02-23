#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    lis = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis.append([name, score])
        scores.add(score)
            
    sec_lowest = sorted(scores)[1] #second lowest mark
    
    sl = []
    for [name, score] in lis:
        if score == sec_lowest:
            sl.append(name)

    for name in sorted(sl):
        print(name, sep='\n')