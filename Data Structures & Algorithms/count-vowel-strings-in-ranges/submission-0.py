class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        sol = []
        validindex = set()
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                validindex.add(i)
        validindex_count = 0
        for query in queries:
            querybeginning = query[0]
            queryend = query[1]
            validindex_count = 0
            for index in range(querybeginning, queryend+1): 
                if index in validindex:
                    validindex_count +=1
                
            sol.append(validindex_count)

        return sol
                    
                






