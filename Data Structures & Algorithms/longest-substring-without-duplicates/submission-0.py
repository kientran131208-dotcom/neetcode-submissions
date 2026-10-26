class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        ans = 1
        if(len(s) == 0):
            return 0
        while(i < len(s)) and (j < len(s)):
            count1 = 1
            for index in range(i, j):
                if(s[index] == s[j]):
                    i = index + 1
                    break
                else:
                    count1+=1
                if(count1 > ans):
                    ans = count1
            j+=1
        return ans