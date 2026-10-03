class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(len(s) == 1):
            return True
        i = 0
        s = ''.join(c for c in s if c.isalpha() or c.isdigit())
        s = s.lower()
        j = len(s) - 1
        if(len(s) == 0):
            return True
        if(len(s) % 2 == 0):
            while True:
                if(i == j - 1):
                    if(s[i] == s[j]):
                        return True
                    else:
                        return False
                if(s[i] == s[j]):
                    i+=1
                    j-=1
                else:
                    return False
            return True
        else:
            while i != j:
                if(s[i] == s[j]):
                    i+=1
                    j-=1
                else:
                    return False
            return True