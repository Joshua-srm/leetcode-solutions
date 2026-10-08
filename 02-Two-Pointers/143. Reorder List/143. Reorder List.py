1class Solution(object):
2    def reorderList(self, head):
3        r = head
4        l = head
5        c = 0
6
7        while r:
8            r = r.next
9            c += 1
10        for i in range((c-1)// 2):
11            l = l.next
12        r = l.next
13        l.next = None
14
15        prev = None
16        curr = r
17        while curr:
18            next_temp = curr.next
19            curr.next = prev
20            prev = curr
21            curr = next_temp
22        l=head
23        while prev:
24            temp1 = l.next
25            temp2 = prev.next
26            l.next=prev
27            prev.next=temp1
28            l=temp1
29            prev=temp2
30        return head
31