class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0
        Ans = 0
        i = 0
        j = len(heights) - 1
        while(i < j):
            Area = 0
            if((heights[i] > maxHeight) or (heights[j] > maxHeight)):
                if(heights[i] > heights[j]):
                    maxHeight = heights[j]
                elif(heights[j] > heights[i]):
                    maxHeight = heights[i]
                Area = min(heights[i], heights[j]) * (j - i)
                if(Area > Ans):
                    Ans = Area
            if(heights[i] > heights[j]):
                j-=1
            else:
                i+=1
        return(Ans)

            