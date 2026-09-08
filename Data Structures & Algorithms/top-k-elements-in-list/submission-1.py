from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for key, val in freqmap.items():
            buckets[val].append(key)
        sol = []
        for bucket in range(len(buckets)-1,-1,-1):
            
            for b in buckets[bucket]:
                sol.append(b)
                if len(sol) == k:
                    return sol
                

