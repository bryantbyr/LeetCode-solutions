class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        t=sorted(nums,reverse=True)
        for i in range(len(nums)):
            nums[i]=str(t.index(nums[i])+1)
            if nums[i]=='1':
                nums[i]="Gold Medal"
            elif nums[i]=='2':
                nums[i]="Silver Medal"
            elif nums[i]=='3':
                nums[i]="Bronze Medal"
        # for i,x in enumerate(nums, 0):
        #     nums[i]=str(t.index(x)+1)
        #     if nums[i]=='1':
        #         nums[i]="Gold Medal"
        #     elif nums[i]=='2':
        #         nums[i]="Silver Medal"
        #     elif nums[i]=='3':
        #         nums[i]="Bronze Medal"
        return nums


s=Solution()
nums=[1,8,9,0,7]
print(s.findRelativeRanks(nums))
