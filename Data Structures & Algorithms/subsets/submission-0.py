class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        i = 0
        self.permute(nums,i,subset,ans)
        return ans

    def permute(self,nums,i,subset,ans):
        if i==len(nums):
            ans.append(subset)               #immediately append the subset to ans when base case is hit since subset takes the new_sub value for new rec call.
            return ans
        self.permute(nums,i+1,subset,ans)    #incremented i but subset is kept unchanged

        new_subset = subset.copy()           #take the right clone and append the new number since i is incremented
        new_subset.append(nums[i])
        self.permute(nums,i+1,new_subset,ans)



        