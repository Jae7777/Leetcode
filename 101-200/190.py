# https://neetcode.io/problems/reverse-bits
# https://leetcode.com/problems/reverse-bits/description/
class Solution:
    def reverseBits(self, n: int) -> int:
        res = n & 1
        for _ in range(31):
            res = res << 1
            n = n >> 1
            res = res | (n & 1)
        return res