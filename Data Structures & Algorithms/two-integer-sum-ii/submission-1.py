class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        Sorted array, so use two pointers instead of a hashmap (O(1) space).

Start one pointer at each end. Loop while left is before right.

Add the two numbers. Too big, move right pointer left. Too small, move left pointer right. Equal, found the pair.

Return both indexes plus one, since the answer is one-indexed.
'''
        l, r = 0, len(numbers) - 1
        while l < r:
            sums = numbers[l] + numbers[r]

            if sums > target:
                r -= 1
            elif sums < target:
                l += 1
            else:
                return [l + 1, r + 1]
