1class Solution(object):
2    def threeSum(self, nums):
3        result = []
4        nums.sort()
5
6        for i in range(len(nums)):
7
8            if i > 0 and nums[i] == nums[i - 1]:
9                continue
10
11            left = i + 1
12            right = len(nums) - 1
13
14            while left < right:
15                total = nums[i] + nums[left] + nums[right]
16
17                if total < 0:
18                    left += 1
19
20                elif total > 0:
21                    right -= 1
22
23                else:
24                    result.append([nums[i], nums[left], nums[right]])
25
26                    while left < right and nums[left] == nums[left + 1]:
27                        left += 1
28
29                    while left < right and nums[right] == nums[right - 1]:
30                        right -= 1
31
32                    left += 1
33                    right -= 1
34
35        return result