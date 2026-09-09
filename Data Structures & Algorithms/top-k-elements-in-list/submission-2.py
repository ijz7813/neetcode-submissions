from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for key, val in freqmap.items():
            buckets[val].append(key)
        sol = []
        for bucket in range(len(buckets)-1, 0, -1):
            for number in buckets[bucket]:

                sol.append(number)
                if len(sol) == k:
                    return sol

