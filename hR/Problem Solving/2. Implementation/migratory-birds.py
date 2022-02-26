#https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    count = [0]*len(arr)
    for i in arr:
        count[i] += 1
    return count.index(max(count))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()