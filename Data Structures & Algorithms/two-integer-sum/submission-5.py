class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in sums:
                return [sums[need], i]
                
            else:
                sums[num] = i