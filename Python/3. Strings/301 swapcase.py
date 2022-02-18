#https://www.hackerrank.com/challenges/swap-case

def swap_case(s):
    newstr = ""
    for letter in s:
        if letter == letter.upper():
            newstr += letter.lower()
        else:
            newstr += letter.upper()
    return newstr

    