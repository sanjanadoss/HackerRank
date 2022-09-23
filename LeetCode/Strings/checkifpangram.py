alph = 'abcdefghijklmnopqrstuvwxyz'
alph = set(alph)
ans = []
def ispan(strarr):
    for i in range(0,len(strarr)):
            a = sum(1 for ch in set(strarr[i]) if 96 < ord(ch) <= 122)
            if a==26:
                ans.append(1)
            else:
                ans.append(0)
    return ans

if __name__ == '__main__':
    strarr = ['the quick brown fox jumps over the lazy dog','abcdehdh','blahblahblah']
    print(ispan(strarr))