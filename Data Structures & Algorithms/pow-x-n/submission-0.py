class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        ans = pow(x,n//2)
        #return 2 * self.myPow(x,n-1)
        if n%2 == 0:
            return ans*ans
        else:
            return ans*ans*x

        