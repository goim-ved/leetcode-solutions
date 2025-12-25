def reverseWords(s: str) -> str:
    words = s.split()
    words.reverse()
    return " ".join(words)

s = " a god no   dog    "
print(reverseWords(s))