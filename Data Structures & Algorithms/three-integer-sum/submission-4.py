class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        k = 0
        res = []

        nums.sort()

        while k < len(nums) - 2:
            l = k + 1
            r = len(nums) - 1

            if (k > 0 and nums[k] == nums[k - 1]):
                k += 1
                continue

            while (l < r):
                if nums[l] + nums[r] + nums[k] == 0:
                    temp = [nums[l], nums[r], nums[k]]
                    res.append(temp)
                    l += 1
                    r -= 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l += 1

                if (nums[l] + nums[r] + nums[k] < 0):
                    l += 1
                elif (nums[l] + nums[r] + nums[k] > 0):
                    r -= 1

            k += 1
            
        
        
        return res
