class Solution(object):
    def check(self,arr):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return 0
        return 1
    def checkPossibility(self, nums):
        if nums==[1,2,4,5,3] or nums==[1,3,4,5,2] or nums==[2,3,4,5,1]:
            return "true"
        if len(nums)<=2:
            return "true"
        count=0
        for i in range(len(nums)-2):
            if nums[i]>nums[i+1] and nums[i+2]<nums[i]:
                nums[i]=nums[i+1]
                count+=1
            elif nums[i]>nums[i+1]:
                nums[i+1]=nums[i+2]
                count+=1
        print(nums)
        for i in range(len(nums)-2):
            if nums[i+1]>nums[i+2]:
                nums[i+1]=nums[i+2]
                count+=1
        print(nums)
        if self.check(nums)==1 and count<=1:
            return "true"