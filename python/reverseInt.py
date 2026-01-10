def reverseInt(x: int) -> int:
    sign = -1 if x < 0 else 1
    x *= sign
    reversedX = int(str(x)[::-1])
    result = sign * reversedX
    if -2**31 < result < 2**31 - 1:
        return result
    return 0

print(reverseInt(-8955))