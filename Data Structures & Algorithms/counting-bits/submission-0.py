class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_count = []        
        for i in range(n+1):
            temp = i  
            count = 0
            while temp != 0:          #0&1 = 0, 1&1= 1, 10&01 -> 1&1 = 1, 11&01 -> 1&1, 100&001 -> 10&01 -> 1&1=1
                if temp&1 == 1:
                    count += 1
                temp >>= 1
            bit_count.append(count)
        return bit_count
            

            # 8 4 2 1

       