1class Solution:
2    def maxArea(self, height):
3        m = 0
4        l = 0
5        r = len(height) - 1
6
7        while l < r:
8
9            area = min(height[l], height[r]) * (r-l)
10
11            if area > m:
12                m=area
13
14            if height[l] < height[r]:
15                l+=1
16            else:
17                r-=1
18        return m
19
20            