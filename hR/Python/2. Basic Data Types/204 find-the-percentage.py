#https://www.hackerrank.com/challenges/finding-the-percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query = input()
    x = student_marks[query]
    print("%.2f" %(sum(x)/len(x)))