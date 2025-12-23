from collections import Counter
def majoryElement(nums: list[int]) -> int:
    count = Counter(nums)
    return count.most_common(1)[0][0]