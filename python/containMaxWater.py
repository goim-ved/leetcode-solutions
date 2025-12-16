def maxWater(heights: list[int]) -> int:
    l, r = 0, len(heights) - 1
    res = 0
    while l < r:
        w = r - l
        area = w * min(heights[l], heights[r])
        res = max(res, area)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res