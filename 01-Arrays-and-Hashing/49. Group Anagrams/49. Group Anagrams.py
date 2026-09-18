1class Solution(object):
2    def groupAnagrams(self, strs):
3        groups={}
4        for i in strs:
5            d={}
6            for j in i:
7                d[j] = d.get(j, 0) + 1
8            key = tuple(sorted(d.items()))
9
10            if key not in groups:
11                groups[key] = []   
12            groups[key].append(i)
13
14
15        return groups.values()
16
17                
18                
19              
20                    
21                    
22                    
23        