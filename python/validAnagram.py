def validAnagram(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)

a = "vedant"
b = "dantv"
print(validAnagram(a, b))