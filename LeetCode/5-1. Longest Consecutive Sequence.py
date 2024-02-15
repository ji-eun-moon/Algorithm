# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums):
        answer = 0

        dic = {}
        for num in nums:
            dic[num] = True

        for num in nums:
            if (num - 1) in dic:
                continue
            target = num + 1
            cnt = 1
            while target in dic:
                target += 1
                cnt += 1
            answer = max(cnt, answer)

        return answer

solve = Solution()
print(solve.longestConsecutive(nums = [100,4,200,1,3,2]))
print(solve.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))