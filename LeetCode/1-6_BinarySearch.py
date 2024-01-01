# https://leetcode.com/problems/binary-search/description/

# 488 ms

class Solution:
    def search(self, nums, target):

        # O(n)
        num_list = []
        for idx, num in enumerate(nums):
            num_list.append([num, idx])

        # O(nlogn)
        num_list.sort(key = lambda x: x[0])

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if num_list[mid][0] > target:
                right -= 1
            elif num_list[mid][0] < target:
                left += 1
            else:
                return num_list[mid][1]

        return -1


solve = Solution()
print(solve.search(nums = [-1,0,3,5,9,12], target = 9))
print(solve.search(nums = [-1,0,3,5,9,12], target = 2))
print(solve.search(nums = [5], target = 5))

# 469 ms - O(logn)
from bisect import bisect_left

class Solution:
    def search(self, nums, target):

        idx = bisect_left(nums, target)
        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1

solve = Solution()
print(solve.search(nums = [-1,0,3,5,9,12], target = 9))
print(solve.search(nums = [-1,0,3,5,9,12], target = 2))
print(solve.search(nums = [5], target = 5))