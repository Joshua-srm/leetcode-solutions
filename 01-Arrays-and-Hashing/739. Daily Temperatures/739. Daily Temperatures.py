1class Solution(object):
2    def dailyTemperatures(self, temperatures):
3        n = len(temperatures)
4        result = [0] * n
5        stack = []
6
7        for i in range(n):
8
9            while stack and temperatures[i] > temperatures[stack[-1]]:
10
11                previous_day = stack.pop()
12
13                result[previous_day] = i - previous_day
14
15            stack.append(i)
16
17        return result