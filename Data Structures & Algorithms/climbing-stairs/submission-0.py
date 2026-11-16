class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*n
        return self.solve(n,dp)

    def solve(self,n,dp):
        if n<=2:
            return n
        if dp[n-1]!=-1:
            return dp[n-1]
        dp[n-1] = self.solve(n-1,dp) + self.solve(n-2,dp)
        return dp[n-1]
        

    
        