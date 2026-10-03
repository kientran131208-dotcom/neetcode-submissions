class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        if 0 not in nums:
            multi = 1
            for i in nums:
                multi*=i
            for i in nums:
                ans.append(int(multi / i))
            return ans
        else:
            multi = 1
            zero_index = []
            for i in range(len(nums)):
                if nums[i] == 0:
                    zero_index.append(i)
            if len(zero_index) > 1:
                ans = [0] * len(nums)
                return ans
            else:
                for i in range(len(nums)):
                    if(nums[i] != 0):
                        ans.append(0)
                        multi *= nums[i]
                    else:
                        ans.append(0)
                ans[nums.index(0)] = multi
                return ans

