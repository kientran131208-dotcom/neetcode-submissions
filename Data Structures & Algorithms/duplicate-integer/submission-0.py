class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = {}
        for i in range(len(nums)):
            if(nums[i] not in ans):
                ans[nums[i]] = 1
            else:
                ans[nums[i]]+=1
            if(ans[nums[i]] >= 2):
                return True
        return False