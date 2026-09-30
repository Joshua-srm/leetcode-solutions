1class Solution(object):
2    def search(self, nums, target):
3        l=0
4        r=len(nums)-1
5        while l<=r:
6            mid=(l+r)//2
7            if nums[mid]==target:
8                return mid
9            elif nums[mid]<target:
10                l=mid+1
11            else:
12                r=mid-1
13        else:
14            return -1
15
16                
17
18                
19
20
21        