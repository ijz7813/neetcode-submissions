from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strssorted = defaultdict(list)
        # for s in strs:
        #     sort = sorted(s)
        #     joined = "".join(sort)
            
        #     strssorted[joined].append(s)
        
        # sol = []
        # for key, val in strssorted.items():
        #     sol.append(val)
        # return sol
        
        strssorted = defaultdict(list)

        # create empty character mapping
       
        for s in strs:
            charactercount = [0]*26
            for char in s:
                charactercount[ord(char)-ord('a')]+=1
            
            
            strssorted[(tuple(charactercount))].append(s)
            
        
        return list(strssorted.values())

