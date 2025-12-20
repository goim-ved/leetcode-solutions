def climbStairs(n: int) -> int:
    if n <= 1:
        return 1
    currentWays, previousWays = 1, 1
    for i in range(n - 1):
        temp = currentWays
        currentWays = currentWays + previousWays
        previousWays = temp

n = 8
print(climbStairs(n))