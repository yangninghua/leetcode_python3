#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (56.35%)
# Likes:    601
# Dislikes: 0
# Total Accepted:    110.3K
# Total Submissions: 193.4K
# Testcase Example:  '[10,15,20]'
#
# 数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
# 
# 每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。
# 
# 请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：cost = [10, 15, 20]
# 输出：15
# 解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
# 
# 
# 示例 2：
# 
# 
# 输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出：6
# 解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
# 
# 
# 
# 
# 提示：
# 
# 
# cost 的长度范围是 [2, 1000]。
# cost[i] 将会是一个整型数据，范围为 [0, 999] 。
# 
# 
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        1.确定dp数组和下标含义 dp[i]爬到楼层i最低花费体力为dp[i]
        2.状态转移方程
        dp[i] = min(dp[i-1], dp[i-2])+cost[i]

        return min(dp[-1], dp[-2])
        3.dp数组初始化
        dp[0]=cost[0]
        dp[1]=cost[1]
        dp[1:]=0
        4.遍历从前到后
        5.验证
        cost = [10, 15, 20]
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        
        10, 15, 35
        return min(15, 35)
        '''
        if cost is None or len(cost)==0:
            return cost
        if len(cost)<2:
            return cost[0]
        dp = [0] * len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2, len(cost), 1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])

# @lc code=end

