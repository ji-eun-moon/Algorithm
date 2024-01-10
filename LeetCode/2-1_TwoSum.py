# https://leetcode.com/problems/two-sum/

# sort, two pointer
class Solution:
    def twoSum(self, nums, target):

        N = len(nums)
        num_list = []

        for idx, num in enumerate(nums):
            num_list.append([num, idx])

        num_list.sort(key = lambda x:x[0])
        left, right = 0, N-1

        while left < right:
            if num_list[left][0] + num_list[right][0] < target:
                left += 1
            elif num_list[left][0] + num_list[right][0] > target:
                right -= 1
            else:
                return [num_list[left][1], num_list[right][1]]

print('SOLUTION 1')
result = Solution()
print('#1', result.twoSum(nums=[2, 7, 11, 15], target=9))
print('#2', result.twoSum(nums=[3, 2, 4], target=6))
print('#3', result.twoSum(nums=[3, 3], target=6))

class Solution:
    def twoSum(self, nums, target):

        num_list = {}

        for idx, num in enumerate(nums):
            if num in num_list:
                num_list[num].append(idx)
            else:
                num_list[num] = [idx]

        for num in nums:
            needed = target - num
            if num == needed:
                if len(num_list[num]) >= 2:
                    return num_list[num]
                else:
                    continue
            elif needed in num_list:
                return [num_list[num][0], num_list[needed][0]]


print('SOLUTION 2')
result = Solution()
print('#1', result.twoSum(nums=[2, 7, 11, 15], target=9))
print('#2', result.twoSum(nums=[3, 2, 4], target=6))
print('#3', result.twoSum(nums=[3, 3], target=6))