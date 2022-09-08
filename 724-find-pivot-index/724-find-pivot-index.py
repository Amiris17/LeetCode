class Solution(object):
    def pivotIndex(self, nums):
        if nums == "":
            return "-1"
        total=sum(nums)
        left_sum = 0
        length = len(nums) - 1
        right_sum=0
        pivot_index=0 # so we need to divert away from summing everything up and instead of looking at hte pivot index
        place_holder=0

        for i in range(len(nums)):
            right_sum=total-nums[i]-left_sum # basically what this is doing is subtracting from the entire total
            print(right_sum)
            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
        return -1