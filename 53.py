nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray( nums) -> int:
    if not nums or len(nums) == None:
        return 0

    total_sum = maxsum = nums[0]

    for i in range(1 ,len(nums)):

        #total_sum = max(nums[i], total_sum + nums[i]) # give running sum
        a=nums[i]
        b=total_sum + nums[i]
        total_sum=max(a,b)
        maxsum = max(maxsum, total_sum) # give a maxsum
    return maxsum

maxSubArray(nums)