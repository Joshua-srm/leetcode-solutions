1class Solution(object):
2
3    def removeDuplicates(self, nums):
4
5        l = 0
6
7        for i in range(1, len(nums)):
8
9            if nums[i] != nums[l]:
10                l += 1
11                nums[l] = nums[i]
12
13        return l + 1