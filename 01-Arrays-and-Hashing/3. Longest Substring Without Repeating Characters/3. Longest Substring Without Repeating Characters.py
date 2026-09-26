1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        left = 0
4        window = set()
5        max_length = 0
6
7        for right in range(len(s)):
8
9            while s[right] in window:
10                window.remove(s[left])
11                left += 1
12
13            window.add(s[right])
14
15            max_length = max(max_length, right - left + 1)
16
17        return max_length