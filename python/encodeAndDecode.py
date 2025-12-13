class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length
            res.append(s[word_start : word_end])
            i = word_end
        return res
    
if __name__ == "__main__":
    solver = Solution()
    input_list = ["neet", "code", "love", "you"]
    
    encoded = solver.encode(input_list)
    print(f"Encoded: {encoded}")

    decoded = solver.decode(encoded)
    print(f"Decoded: {decoded}")