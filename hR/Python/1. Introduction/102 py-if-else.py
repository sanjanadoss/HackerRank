# https://www.hackerrank.com/challenges/py-if-else/problem
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1 or 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')