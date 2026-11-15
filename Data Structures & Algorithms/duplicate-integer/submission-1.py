class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = set()

        for num in nums:
            if num in sets:
                return True
            else:
                sets.add(num)

        return False