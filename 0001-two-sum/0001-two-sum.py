class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map={}
        for i,n in enumerate(nums):
            comp=target-n
            if comp not in comp_map:
                comp_map[n]=i
            else:
                return [comp_map[comp],i]