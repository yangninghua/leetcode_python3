#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (52.24%)
# Likes:    1768
# Dislikes: 0
# Total Accepted:    502.1K
# Total Submissions: 957.8K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        1.确定dp数组及下标含义 i阶楼层有dp[i]种不同的爬法
        2.状态转移方程,dp[i]=dp[i-1]+dp[i-2]
        3.dp[i] 初始化
        dp[1]=1 dp[2]=2(1+1;2)
        4.dp[i]遍历顺序
        dp[i]由dp[i-1]和dp[i-2]计算，顺序从前往后
        '''
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        dp = [0 for _ in range(n+1)]
        dp[1]=1;dp[2]=2
        for i in range(3, n+1, 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# @lc code=end

