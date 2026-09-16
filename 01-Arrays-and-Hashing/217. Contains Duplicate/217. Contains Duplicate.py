1class Solution(object):
2    def containsDuplicate(self, nums):
3        hset=set()
4        for i in nums:
5            if i in hset:
6                return True
7            hset.add(i)
8        return False