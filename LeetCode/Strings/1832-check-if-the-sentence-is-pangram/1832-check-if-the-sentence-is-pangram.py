class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alph = 'abcdefghijklmnopqrstuvwxyz'
        a = sum(1 for i in set(sentence) if 96<ord(i)<=122)
        if a==26:
            return True
        else:
            return False