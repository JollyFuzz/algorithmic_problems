# https://leetcode.com/problems/climbing-stairs/description/
memo = {
    1: 1,
    2: 2, 
    3: 3
}
class Solution:
    def climbStairs_v1(self, n: int) -> int:
        if n in memo:
            return memo[n]
        
        root1 = self.climbStairs(n-1)
        root2 = self.climbStairs(n-2)

        memo[n] = root1 + root2

        return root1 + root2
    
    def climbStairs(self, n: int) -> int:
        prev, curr = 1
        for i in range(2, n+1):
            temp = curr + prev
            prev = curr
            curr = temp

        return curr