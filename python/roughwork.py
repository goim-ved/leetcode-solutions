def equilibriumIndex(nums: list[int]) -> int:
    numss = sorted(nums)
    l, r = 0, len(numss) - 1
    sumL = 0
    sumR = 0
    while l < r:
        sumL = numss[l] + numss[l+1]
        sumR = numss[r] + numss[r-1]
        if sumL == sumR and ((r-1) - (l+1) == 2):
            return l + 2
        else:
            l += 1
            r -= 1
    return None