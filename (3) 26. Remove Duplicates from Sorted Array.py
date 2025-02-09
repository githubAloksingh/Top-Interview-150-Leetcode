class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums=sorted(set(nums))
        k=len(unique_nums)
        for i in range(k):
            nums[i]=unique_nums[i]
        return k
        




# Approach: Two-Pointer Technique
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
        
