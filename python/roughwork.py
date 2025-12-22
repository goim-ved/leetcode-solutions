def maxSubArray(nums: list[int]) -> int:
    currentSum = 0
    maxSum = nums[0]
    for num in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += num
        maxSum = max(maxSum, currentSum)
    return maxSum