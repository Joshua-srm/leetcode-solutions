1class Solution(object):
2
3    def topKFrequent(self, nums, k):
4
5        d = {}
6
7        for i in nums:
8            d[i] = d.get(i, 0) + 1
9
10        l = sorted(d, key=lambda x: d[x], reverse=True)
11
12        return l[:k]
13        