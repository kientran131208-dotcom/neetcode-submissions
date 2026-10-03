class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = {}
        for i in s:
            if(i not in ans):
                ans[i] = 1
            else:
                ans[i]+=1
        for i in t:
            if(i in ans):
                ans[i]-=1
            else:
                return False
            if(ans[i] < 0):
                return False
        if(max(ans.values()) != 0):
            return False
        return True