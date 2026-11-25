class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        # seen = set()
        # for value in nums:
        #     if value not in seen:
        #         seen.add(value)
        #     else:
        #         return True
        # return False
        