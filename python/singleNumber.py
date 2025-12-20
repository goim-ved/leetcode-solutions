def singleNumber(nums: list[int]) -> int:
    mySet = set()
    for i in range(len(nums)):
        if nums[i] not in mySet:
            mySet.add(nums[i])
        else:
            mySet.remove(nums[i])
    myList = list(mySet)
    return myList[0]

trial = [4,1,2,1,2]
print(singleNumber(trial))