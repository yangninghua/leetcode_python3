#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
# https://leetcode-cn.com/problems/integer-break/description/
#
# algorithms
# Medium (60.05%)
# Likes:    561
# Dislikes: 0
# Total Accepted:    96.6K
# Total Submissions: 160.5K
# Testcase Example:  '2'
#
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
# 
# 示例 1:
# 
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 
# 示例 2:
# 
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 
# 说明: 你可以假设 n 不小于 2 且不大于 58。
# 
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        给定一个正整数 n，将其拆分为 至少两个 正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
        1.dp[i] 正整数i的最大乘积为dp[i]
        2.
        dp[i] = max(1 * (i-1), 2 * (i-2), ..., i-1 * (1), 1*dp[i-1], 2*dp[i-2], ..., i-1*dp[1])
        return dp[n]
        3.初始化
        dp[1]=1
        dp[2]=1
        dp[3]=2
        4.遍历
        dp[i]的推导 从前往后
        5.
        '''
        if n==2:
            return 1
        if n==3:
            return 2
        dp = [0]*(n+1)
        dp[2]=1
        dp[3]=2
        for i in range(4, n+1, 1):
            for j in range(1, i-1, 1):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]

# @lc code=end

