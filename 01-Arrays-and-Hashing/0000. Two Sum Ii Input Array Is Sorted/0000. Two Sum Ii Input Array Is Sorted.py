1class Solution(object):
2    def twoSum(self, numbers, target):
3        l = 0
4        r = len(numbers) - 1
5
6        while l < r:
7            total = numbers[l] + numbers[r]
8
9            if total > target:
10                r -= 1
11            elif total < target:
12                l += 1
13            else:
14                return [l + 1, r + 1]