class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]        
        dp = [-1]*len(nums)
        possibility1 = self.solve(0,nums,dp,len(nums)-2)
        dp = [-1]*len(nums)
        possibility2 = self.solve(1,nums,dp,len(nums)-1)
        return max(possibility1,possibility2)
    
    def solve(self,index,nums,dp,end):
        if index > end:
            return 0
        if dp[index]!=-1:
            return dp[index]
        pick = nums[index] + self.solve(index+2,nums,dp,end)
        skip = self.solve(index+1,nums,dp,end)
        dp[index] = max(pick,skip)
        return dp[index]
        
        