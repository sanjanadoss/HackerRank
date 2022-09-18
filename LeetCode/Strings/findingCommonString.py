#https://leetcode.com/problems/find-common-characters/
def commonChars(self, A: List[str]) -> List[str]:
    check = list(A[0]) #storing first item of the array
    for word in A[1:]:
        newCheck = []
        for c in word:
            if c in check:
                newCheck.append(c)
                check.remove(c)
        check = newCheck #updating newCheck to hold common letters and using it for checking the next item
    return check