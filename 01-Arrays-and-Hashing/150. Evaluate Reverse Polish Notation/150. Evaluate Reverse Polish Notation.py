1class Solution(object):
2    def evalRPN(self, tokens):
3        stack = []
4
5        for token in tokens:
6
7            if token in [+, -, *, /]:
8
9                b = stack.pop()
10                a = stack.pop()
11
12                if token == +:
13                    result = int(b)+int(a)
14
15                elif token == -:
16                    result = int(a)-int(b)
17
18                elif token == *:
19                    result = int(b)*int(a)
20
21                else:
22                    result = abs(a) // abs(b)
23                    if (a < 0) != (b < 0):
24                        result = -result
25
26                stack.append(result)
27
28            else:
29                stack.append(int(token))
30
31        return stack[-1]