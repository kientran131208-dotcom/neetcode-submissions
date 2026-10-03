class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = {}
        print(len(nums))
        for num in nums:
            if(num not in ans):
                ans[num] = 1
            else:
                ans[num]+=1
            if(len(nums) / 2 < ans[num]):
                return num