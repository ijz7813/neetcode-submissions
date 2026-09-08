from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        # now need to fill bucket with the freqmap
        for key, val in freqmap.items():
            bucket[val].append(key)
        
        #print(bucket)
        sol = []
        for index in range(len(bucket)-1, 0, -1):
            for i in bucket[index]:
                sol.append(i)
                if len(sol) == k:
                    return sol
