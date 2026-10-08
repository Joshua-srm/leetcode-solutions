1class Solution(object):
2    def removeNthFromEnd(self, head, n):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        l = dummy
7        r = dummy
8
9        for i in range(n):
10            r=r.next
11        while r.next:
12            r=r.next
13            l=l.next
14        l.next=l.next.next
15        return dummy.next
16