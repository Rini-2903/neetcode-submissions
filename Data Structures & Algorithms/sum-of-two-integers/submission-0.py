class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit_sum_wdt_carry = a^b
        bit = (a&b) << 1
        return bit + bit_sum_wdt_carry




        