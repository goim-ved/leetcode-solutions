def longestConsecutive(nums: list[int]) -> int:
    nums2 = set(nums)
    longest = 0
    for num in nums2:
        if (num - 1) not in nums2:
            length = 0
            while (num + length) in nums2:
                length += 1
            longest = max(length, longest)
    return longest