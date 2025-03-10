# https://neetcode.io/problems/rotate-matrix
# https://leetcode.com/problems/rotate-image/description/
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        matrix.reverse()
        # transpose
        for i in range(N):
            for j in range(i + 1, N):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp