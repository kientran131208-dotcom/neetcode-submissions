class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        for i in nums:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i]+=1
        sorted_ans = dict(sorted(ans.items(), key = lambda x : x[1], reverse = True))
        riel_ans = []
        for x in sorted_ans.keys():
            riel_ans.append(x)
            if(len(riel_ans)== k):
                return riel_ans