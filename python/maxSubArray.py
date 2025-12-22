def maxSubArray(nums: list[int]) -> int:
    currentSums = 0
    maxSum = nums[0]
    for num in nums:
        if currentSums < 0:
            currentSums = 0
        currentSums += num
        maxSum = max(maxSum, currentSums)
    return maxSum