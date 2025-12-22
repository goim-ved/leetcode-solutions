def moveZeroes(self, nums: list[int]) -> None:
    lastZeroAt = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastZeroAt] = nums[i]
            lastZeroAt += 1
    for i in range(lastZeroAt, len(nums)):
        nums[i] = 0