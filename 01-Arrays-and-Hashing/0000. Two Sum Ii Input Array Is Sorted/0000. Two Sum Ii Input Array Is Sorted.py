class Solution(object):
    def twoSum(self, numbers, target):
        
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        
        st=0
        end=len(numbers)-1
        while (st<end):
            if numbers[st]+numbers[end]==target:
                return [(st+1), (end+1)]
                break
            elif numbers[st]+numbers[end]>target:
                end-=1
            else:
                st+=1
