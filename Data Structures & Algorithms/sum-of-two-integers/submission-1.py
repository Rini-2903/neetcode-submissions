class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit_sum_wdt_carry = a^b
        bit_with_carry = (a&b) << 1
        return bit_with_carry + bit_sum_wdt_carry




        