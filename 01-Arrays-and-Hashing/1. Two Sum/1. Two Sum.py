1class Solution(object):
2    def twoSum(self, nums, target):
3        seen = {}  # value -> index
4        for i, num in enumerate(nums):
5            nt = target - num
6            if nt in seen:
7                return [seen[nt], i]
8            seen[num] = i
9