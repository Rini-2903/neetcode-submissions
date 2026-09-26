class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF          #11111111111111111111111111111111
        mask_int = 0x7FFFFFFF      #01111111111111111111111111111111 (largest positive number)
        while b!=0:
            bit_sum_wdt_carry = (a^b) & mask      #to handle negative integers
            bit_with_carry = ((a&b) << 1) & mask       #(01 -> 10)
            
            a = bit_sum_wdt_carry
            b = bit_with_carry
             
        if a<= mask_int:
            return a
        else:
            return ~(a^mask)

       




        