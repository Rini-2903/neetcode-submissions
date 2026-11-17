class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        return self.solve(0,nums,dp)
    
    def solve(self,index,nums,dp):
        if index >= len(nums):
            return 0
        if dp[index]!=-1:
            return dp[index]
        pick =  nums[index] + self.solve(index+2,nums,dp)
        skip = self.solve(index+1,nums,dp)

        dp[index] = max(pick,skip)
        return dp[index]


        