1class Solution(object):
2    def isPalindrome(self, s):
3        m=[]
4        for i in s:
5            if i.isalpha():
6                m.append(i.lower())
7        k=m[::-1]
8        if k==m:
9            return True
10        else:
11            return False
12