class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sw = "".join(sorted(word))
            if sw in anagrams:
                anagrams[sw].append(word)
            else:
                anagrams[sw] = [word]
        return list(anagrams.values())        