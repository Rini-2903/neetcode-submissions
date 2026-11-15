class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in range (len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            
        maximum = 0
        ans = 0
        for key in freq:
            if freq[key] > maximum:
                maximum = freq[key]
                ans = key
        return ans
        