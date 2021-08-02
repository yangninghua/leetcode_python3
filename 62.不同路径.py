#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (65.48%)
# Likes:    1057
# Dislikes: 0
# Total Accepted:    280.9K
# Total Submissions: 427.8K
# Testcase Example:  '3\n7'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 
# 问总共有多少条不同的路径？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：m = 3, n = 7
# 输出：28
# 
# 示例 2：
# 
# 
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
# 
# 
# 示例 3：
# 
# 
# 输入：m = 7, n = 3
# 输出：28
# 
# 
# 示例 4：
# 
# 
# 输入：m = 3, n = 3
# 输出：6
# 
# 
# 
# 提示：
# 
# 
# 1 
# 题目数据保证答案小于等于 2 * 10^9
# 
# 
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        1.dp[i][j] 表示机器人从(0,0)到达(i,j)的不同路径个数
        2.状态转换方程：
        只能向右向下
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        3.初始化
        (0,0)到(0,j)的不同路径个数为1
        (0,0)到(i,0)的不同路径个数为1
        4.遍历顺序
        由状态转移方程，从上到下，从左到右
        5.

        '''
        dp = [[0]*n for _ in range(m)]
        for temp in range(m): dp[temp][0]=1
        for temp in range(n): dp[0][temp]=1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


# @lc code=end

