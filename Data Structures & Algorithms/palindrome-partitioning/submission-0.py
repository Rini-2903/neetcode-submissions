class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        current_partitions = []
        self.palin_partition(s,current_partitions,ans)
        return ans

    def palin_partition(self,s,current_partitions,ans):
        if s == "":
            ans.append(current_partitions.copy())
            return

        for partitions in range(1,len(s)+1):
            prefix = s[:partitions]
            prefix_remaining = s[partitions:]
            if self.isPalin(prefix):
                current_partitions.append(prefix)
                self.palin_partition(prefix_remaining,current_partitions,ans)
                current_partitions.pop()
    
    def isPalin(self,s):
        l = 0
        r = len(s) - 1
        while l<r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        