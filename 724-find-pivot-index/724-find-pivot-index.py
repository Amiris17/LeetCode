class Solution(object):
    def pivotIndex(self, nums):
        if nums == "":
            return "-1"

        left_sum = 0
        right_sum= 0



        for i in range(len(nums)):
            left_sum += nums[i]
            right_sum=sum(nums[i:])
           
            if left_sum==right_sum:
                return i

        return -1