from collections import Counter
def findAllDuplis(nums: list[int]) -> list[int]:
    count = Counter(nums)
    dups = [num for num, freq in count.items() if freq == 2]
    return dups