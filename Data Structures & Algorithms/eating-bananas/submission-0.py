class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def binary_search(min_val, max_val, h, arr):
            l = min_val
            r = max_val
            ans = 0
            max_ans = max_val
            while l <= r:
                mid = int((l + r) / 2)
                times = 0
                for i in arr:
                    if (i % mid) != 0:
                        times += int(i / mid) + 1
                    elif (i % mid) == 0:
                        times+= int(i / mid)
                    if(times > h):
                        l = mid + 1
                        break
                if(times <= h):
                    ans = mid
                    r = mid - 1
                    if(max_ans >= ans):
                        max_ans = ans 
            return max_ans
        return binary_search(1, max(piles), h, piles)