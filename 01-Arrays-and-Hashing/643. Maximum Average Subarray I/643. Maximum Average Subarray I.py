1class Solution(object):
2    def findMaxAverage(self, nums, k):
3        s=sum(nums[:k])
4        r=len(nums)
5        ns=s
6        for i in range(k,r):
7            s=s-nums[i-k]+nums[i]
8            ns=max(ns,s)
9        m=float(ns)/k
10        return m
11
12
13
14        