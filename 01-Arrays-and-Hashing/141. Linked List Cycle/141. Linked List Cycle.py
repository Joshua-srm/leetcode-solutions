1
2class Solution(object):
3    def hasCycle(self, head):
4    
5        seen = set()
6        cur = head
7        while cur:
8            if cur in seen:
9                return True
10            seen.add(cur)
11            cur = cur.next
12        return False
13        