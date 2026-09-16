class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        joined = "".join([i for i in s if i.isalnum()])
        l, r = 0, len(joined)-1
        while l <= r:
            if joined[l].casefold() == joined[r].casefold():
                l+=1
                r-=1
            else:
                return False
        
        return True