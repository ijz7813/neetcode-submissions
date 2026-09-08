class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        currlen = 0
        
        #make sure it doesnt go over
        strset=set()
        while r < len(s):
            # check to see if the next character is in the set
            # if it isnt in the set it will increase the length 
            if s[r] not in strset:
                currlen = max(currlen,r-l+1)
                strset.add(s[r])
                r+=1
            #elif s[r] in strset and 
            else:
                strset.remove(s[l])
                l+=1
                
            
            #if it is in the set, the max should reset to 0 since
            # it is starting the process over again
            # the left pointer should also be 
            
                
           
        return currlen
