1class Solution(object):
2    def isValid(self, s):
3        st = []
4
5        pairs = {
6            ')': '(',
7            ']': '[',
8            '}': '{'
9        }
10
11        for ch in s:
12            if ch in pairs.values():
13                st.append(ch)
14            else:
15
16                # Step 3: Check if the stack is empty
17                if not st:
18                    return False
19
20                # Step 4: Check if the top of the stack matches
21                # the expected opening bracket
22                elif st[-1]!=pairs[ch]:
23                    return False
24
25                # Step 5: If it matches, remove the top element
26                else:
27                    st.pop()
28
29        
30        if st==[]:
31            return True
32