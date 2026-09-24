class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            current_bit = n&1
            n>>=1
            ans<<=1
            ans = ans|current_bit
        return ans

        