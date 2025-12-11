def twoSum(nums: list, target: int) -> list:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return None

nums = [2,3,4,5]
target = 9

print(twoSum(nums, target))