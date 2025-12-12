def containsDuplicate(nums: list) -> bool:
    nums2 = set(nums)
    return len(nums2) != len(nums)

nums = [2,4,5,6]
print(containsDuplicate(nums))