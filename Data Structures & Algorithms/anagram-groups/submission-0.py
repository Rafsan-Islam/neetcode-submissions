class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}

        for char in strs:
            key = "".join(sorted(char))
            if key in ana:
                ana[key].append(char)
            else:
                ana[key] = [char]

        return list(ana.values())