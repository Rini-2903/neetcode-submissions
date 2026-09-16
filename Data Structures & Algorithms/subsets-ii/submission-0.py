class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        i = 0
        subset = []
        ans = []
        visited = [0]*len(nums)
        nums.sort()
        self.solve(nums,i,subset,ans,visited)
        return ans
    def solve(self,nums,i,subset,ans,visited):
        if i == len(nums):
            ans.append(subset)
            return ans

        #Don't Take left clones and keep on iterating i
        self.solve(nums,i+1,subset,ans,visited)

        #Don't take right subsets sometimes when previous duplicate is not taken and return to the previous recursion call; or else duplicate subsets will be generated
        if i > 0 and nums[i] == nums[i-1] and visited[i-1] == False:
            return
        
        #Take the base cases after right and left branches generate the subsets equal to array size and when prev duplicate present is true
        visited[i] = True
        new_subset = subset.copy()
        new_subset.append(nums[i])
        self.solve(nums,i+1,new_subset,ans,visited)
        visited[i] = False


        