1
2class Solution(object):
3    def mergeTwoLists(self, list1, list2):
4        dummy = tail = ListNode()
5
6        while list1 and list2:
7            if list1.val < list2.val:
8                tail.next = list1
9                list1 = list1.next
10            else:
11                tail.next = list2
12                list2 = list2.next
13            tail = tail.next
14
15        tail.next = list1 or list2
16
17        return dummy.next
18
19