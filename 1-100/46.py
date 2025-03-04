# https://neetcode.io/problems/permutations
# https://leetcode.com/problems/permutations/description/
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = set(nums)
        def createPermute(used, currPerm):
            if len(currPerm) == len(nums):
                res.append(currPerm)
                return
            for n in nums - used:
                createPermute(used | set([n]), currPerm + [n])
        createPermute(set(), [])
        return res