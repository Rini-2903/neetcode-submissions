class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = []
        self.solve(nums,ans,used)
        return ans
    
    def solve(self,nums,ans,used):
        if len(used) == len(nums):
            ans.append(used.copy())
            return ans

        for i in range(len(nums)):
            if nums[i] not in used:
                used.append(nums[i])
                self.solve(nums,ans,used)
                used.pop()




        