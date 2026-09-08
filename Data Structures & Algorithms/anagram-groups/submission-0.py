from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strssorted = defaultdict(list)
        for s in strs:
            sort = sorted(s)
            joined = "".join(sort)
            if joined not in strssorted:
                strssorted[joined].append(s)
            else:
                strssorted[joined].append(s)
        
        sol = []
        for key, val in strssorted.items():
            sol.append(val)
        return sol
        