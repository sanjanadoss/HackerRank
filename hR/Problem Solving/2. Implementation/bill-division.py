#https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, k, b):
    z = bill[k]
    while bill[k]==z:
        bill.remove(bill[k])
    x = sum(bill)//2
    if b>x:
        print(b-x)
    else:
        print("Bon Appetit")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)