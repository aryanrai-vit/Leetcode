class Solution:
    def findMin(self, nums: List[int]) -> int:
        def finding(nums,left,right):
            if left == right:
                return nums[left]
            elif len(nums) == 2:
                if nums[left] < nums[right]:
                    return nums[left]
                else:
                    return nums[right]
            else:
                mid = left +(right-left) //2
                leftmin = finding(nums,left,mid)
                rightmin = finding(nums,mid+1,right)
                if leftmin < rightmin:
                    return leftmin
                else:
                    return rightmin
        return finding(nums,0,len(nums)-1)
        