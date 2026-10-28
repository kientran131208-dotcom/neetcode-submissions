class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_check = ""
        i = 0
        j = len(s1) - 1
        new_s1 = "".join(sorted(s1))
        while(j < len(s2)):
            check = "".join(sorted(s2[i:j+1]))
            if(check == new_s1):
                return True
            else:
                i+=1
                j+=1
        return False