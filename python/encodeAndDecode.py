def encode(strs: list[str]) -> str:
    encodedString = ""
    for s in strs:
        encodedString += str(len(s)) + "#" + s
    return encodedString

def decode(s: str) -> list[str]:
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        wordStart = j + 1
        wordEnd = wordStart + length
        res.append(s[wordStart:wordEnd])
        i = wordEnd
    return res  