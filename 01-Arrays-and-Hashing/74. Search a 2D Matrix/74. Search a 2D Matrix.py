1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        l=0
4        r=(len(matrix[0])*len(matrix))-1
5        while l<=r:
6            mid=(l+r)//2
7            k=mid//len(matrix[0])
8            m=mid%len(matrix[0])
9            if matrix[k][m]==target:
10                return True
11            elif matrix[k][m]>target:
12                r=mid-1
13            else:
14                l=mid+1
15        else:
16            return False