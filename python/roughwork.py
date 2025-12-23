from collections import Counter

nums = [4,3,2,7,8,2,3,1]
count = Counter(nums)
dups = [num for num, freq in count.items() if freq == 2]
print(dups)