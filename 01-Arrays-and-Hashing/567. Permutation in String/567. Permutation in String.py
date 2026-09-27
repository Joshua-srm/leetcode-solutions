1class Solution(object):
2    def checkInclusion(self, s1, s2):
3        d1={}
4        if len(s1)>len(s2):
5            return False
6        for i in s1:
7            d1[i]=d1.get(i,0)+1
8        k=len(s1)
9        a=0
10        d2={}
11        for m in range(k):
12            d2[s2[m]]=d2.get(s2[m],0)+1
13        if d2==d1:
14            return True
15        for j in range(k,len(s2)):
16            d2[s2[j-k]]-=1
17            if d2[s2[j-k]]==0:
18                del d2[s2[j-k]]
19            d2[s2[j]]=d2.get(s2[j],0)+1
20            if d2==d1:
21                return True
22                break
23        else:
24            return False
25
26