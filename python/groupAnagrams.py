from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)
    for s in strs:
        sorted_s = sorted(s)
        key = "".join(sorted_s)
        anagram_map[key].append(s)
    return list(anagram_map.values())