1class Solution(object):
2    def search(self, nums, target):
3        l=0
4        r=len(nums)-1
5        while l<=r:
6            mid=(l+r)//2
7            if nums[mid]==target:
8                return mid
9            if nums[l]<=nums[mid]:
10                if nums[l]<= target< nums[mid]:
11                    r=mid-1
12                else:
13                    l=mid+1
14            else:
15                if nums[mid]<target<=nums[r]:
16                    l=mid+1
17                else:
18                    r=mid-1
19        else:
20            return -1