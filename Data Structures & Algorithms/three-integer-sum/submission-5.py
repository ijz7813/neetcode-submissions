class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsorted = sorted(nums)

        
        sol = []
        for i in range(len(numsorted)-1):
            if i > 0 and numsorted[i] == numsorted[i - 1]:
                continue
            l = i+1
            r = len(numsorted)-1
            if numsorted[i] > 0:
                return sol
            while l < r:
                curr = numsorted[i] + numsorted[l] + numsorted[r]
                
                if curr > 0:
                    # -1 0 2 3 4
                    r -=1
                elif curr < 0:
                    l+=1
                    
                else:
                    sol.append([numsorted[i], numsorted[l], numsorted[r]])
                    l+=1
                    r-=1
                    while l < r and numsorted[l] == numsorted[l - 1]:
                        l += 1
        return sol

                