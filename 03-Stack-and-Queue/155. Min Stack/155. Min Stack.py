1class MinStack(object):
2    global m
3    def __init__(self):
4        self.st=[]
5        self.mn=[]
6
7    def push(self, value):
8        self.st.append(value)
9        if not self.mn:
10            self.mn.append(value)
11        else:
12            self.mn.append(min(value, self.mn[-1]))
13               
14
15    def pop(self):
16        self.st.pop()
17        self.mn.pop()    
18
19    def top(self):
20        return self.st[-1]
21
22
23    def getMin(self):
24        return self.mn[-1]
25        
26        
27        
28
29
30# Your MinStack object will be instantiated and called as such:
31# obj = MinStack()
32# obj.push(value)
33# obj.pop()
34# param_3 = obj.top()
35# param_4 = obj.getMin()