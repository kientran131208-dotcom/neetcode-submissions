class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        l = 0
        r = len(matrix) - 1

        def search(nums, tar):

            l = 0
            r = len(nums) - 1

            while l <= r:

                mid = (l + r) // 2

                if nums[mid] > tar:
                    r = mid - 1

                elif nums[mid] < tar:
                    l = mid + 1

                else:
                    return True

            return False

        while l <= r:

            mid = (l + r) // 2

            first = matrix[mid][0]
            last = matrix[mid][-1]


            if target > last:
                l = mid + 1

            elif target < first:
                r = mid - 1

            else:
                return search(matrix[mid], target)

        return False