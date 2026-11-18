class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        nums[i] is the amount of times we will go through and skip it, but we will ultimitaly start from zero. 

        ohhh, so if we loop through the index untill we get the element that is the one we want to skip we just multiply every element to its left and then multiply everything to its right then we can just multiply up the values and then do this for each and every pass that happens then we can just return the outputs, and im guessing we can just create an empty list for that and add the output to the list every singe time.

a faster method would be if we just keep going and we multiply the left then the next pass that happens we just muliply the last output by the next number
'''
        output = [1] * len(nums)
        l = 1

        for i in range(len(nums)):
            output[i] = l
            l *= nums[i]

        r = 1

        for i in range(len(nums)- 1, -1 ,-1):
            output[i] *= r
            r *= nums[i]

        return output