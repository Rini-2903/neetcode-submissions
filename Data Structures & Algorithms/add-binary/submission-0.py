class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry_bit = 0
        i = len(a) - 1              #using 1 pointers
        j = len(b) - 1
        while i>=0 or j>=0 or carry_bit>0:
            if i>=0:
                digitA = int(a[i])
            else:
                digitA = 0
            if j>=0:
                digitB = int(b[j])
            else:
                digitB = 0
            total = digitA + digitB + carry_bit
            result_bit = total % 2            #bit w/o carry
            res.append(result_bit)
            carry_bit = total // 2         #bit carrrying carry

            i-=1
            j-=1
        res.reverse()
        return ''.join(map(str,res))             

       
        