1class Solution(object):
2
3    def longestCommonPrefix(self, strs):
4
5        if not strs:
6            return 
7
8        min_len = len(strs[0])
9        for k in strs:
10            if len(k)<min_len:
11                min_len=len(k)
12
13        ans = 
14
15        for i in range(min_len):
16
17            for j in range(1, len(strs)):
18                if strs[0][i] != strs[j][i]:
19                    return ans
20
21            ans += strs[0][i]
22
23        return ans