def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    num = 4
    print(search(nums, num))