class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        currlen = 0
        strset = set()
        while r < len(s):
            if s[r] not in strset:
                currlen = max(currlen, r-l+1)
                strset.add(s[r])
                
                r+=1
            else:
                strset.remove(s[l])
                l+=1
        return currlen