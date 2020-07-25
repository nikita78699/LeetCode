#  https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a = 1
        b = 2
        for i in range(n - 2):
            c = a + b
            a = b
            b = c
        return b
