from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        for i,s in enumerate(strs):
            sorted_key = "".join(sorted(s))
            my_map[sorted_key].append(strs[i])
        return list(my_map.values())