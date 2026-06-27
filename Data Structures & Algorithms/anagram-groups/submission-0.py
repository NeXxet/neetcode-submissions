class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            sortedString = "".join(sorted(s))
            map[sortedString].append(s)
        
        return list(map.values())