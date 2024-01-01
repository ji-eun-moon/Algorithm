# https://leetcode.com/problems/two-sum/

# 4307 ms - O(n^2)
class Solution:
    def twoSum(self, nums, target):
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]

result = Solution()
print('#1')
print(result.twoSum(nums=[2, 7, 11, 15], target=9))
print(result.twoSum(nums=[3, 2, 4], target=6))
print(result.twoSum(nums=[3, 3], target=6))

# 146 ms - O(nlogn)
class Solution:
    def twoSum(self, nums, target):
        N = len(nums)

        # O(n)
        num_list = []
        for idx, num in enumerate(nums):
            num_list.append([num, idx])

        # O(nlogn)
        num_list.sort(key=lambda x: x[0])
        left, right = 0, N-1

        # O(n)
        while left < right:
            if num_list[left][0] + num_list[right][0] < target:
                left += 1
            elif num_list[left][0] + num_list[right][0] > target:
                right -= 1
            else:
                return [num_list[left][1], num_list[right][1]]

result = Solution()
print('#2')
print(result.twoSum(nums=[2, 7, 11, 15], target=9))
print(result.twoSum(nums=[3, 2, 4], target=6))
print(result.twoSum(nums=[3, 3], target=6))

# 86 ms - O(n)
class Solution:
    def twoSum(self, nums, target):

        # O(n)
        dic = {}
        for idx, num in enumerate(nums):
            if num not in dic:
                dic[num] = [idx]
            else:
                dic[num].append(idx)

        # O(n)
        for num in nums:
            remain = target - num
            # O(1)
            if num == remain:
                if len(dic[num]) >= 2:
                    return dic[num]
                else:
                    continue
            elif remain in dic:
                return [dic[num][0], dic[remain][0]]

result = Solution()
print('#3')
print(result.twoSum(nums=[2, 7, 11, 15], target=9))
print(result.twoSum(nums=[3, 2, 4], target=6))
print(result.twoSum(nums=[3, 3], target=6))