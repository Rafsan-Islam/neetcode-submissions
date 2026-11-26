class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort the array first so I can use two pointers then have an outer loop that moves the fixed number one step at a time and for each fixed number run two pointers on the numbers after it with left starting right after the fixed number and right starting at the end then add all three and if the sum is too big move the right pointer left and if it is too small move the left pointer right and if it equals zero save the triplet then collect every triplet in a list and return it at the end and I still need to figure out how to skip duplicates
        '''

        three = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sums = nums[l] + nums[r] + nums[i]
                if sums == 0:
                    three.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif sums > 0:
                    r -= 1
                else:
                    l += 1
        return three