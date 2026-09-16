1class Solution(object):
2    def isAnagram(self, s, t):
3
4        if len(s) != len(t):
5            return False
6
7        d1 = {}
8        d2 = {}
9
10        for ch in s:
11            d1[ch] = s.count(ch)
12
13        for ch in t:
14            d2[ch] = t.count(ch)
15
16        return d1 == d2
17
18            
19        
20        