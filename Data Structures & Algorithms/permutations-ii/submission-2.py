class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = []
        nums.sort()
        visited = [False]*len(nums)
        self.solve(nums,ans,used,visited)
        return ans
    
    def solve(self,nums,ans,used,visited):
        if len(used) == len(nums):
            ans.append(used.copy())
            return ans
        
        for i in range(len(nums)):
            if visited[i] or i>0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            visited[i] = True
            used.append(nums[i])
            self.solve(nums,ans,used,visited)   
            used.pop()                    
            visited[i] = False

        