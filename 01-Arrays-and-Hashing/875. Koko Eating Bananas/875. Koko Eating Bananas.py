1class Solution(object):
2    def minEatingSpeed(self, piles, h):
3        l=1
4        r=max(piles)
5        while l<=r:
6            mid=(l+r)//2
7            hours = 0
8            for i in piles:
9                hours += (i + mid - 1) // mid
10            if hours<=h:
11                r=mid-1
12            else:   
13                l=mid+1
14        return l
15
16
17        