from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        lst = []

        for key, val in count.most_common(k):
            lst.append(key)

        return lst