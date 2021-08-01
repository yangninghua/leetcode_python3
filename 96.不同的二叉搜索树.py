#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (69.74%)
# Likes:    1249
# Dislikes: 0
# Total Accepted:    143.3K
# Total Submissions: 205.1K
# Testcase Example:  '3'
#
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：5
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        #给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
        空节点 种数1
        1个节点 种数1
        2个节点 种数2
            2
        1 

        1
            2
        3个节点 种数5
第1
            1
                    2
                        3
第2
            1
                    3
                2
第3
            2
        1       3
第4
            3
    2        
1
第5
            3
    1        
        2


        1.dp[i] i组成的互不相同的 二叉搜索树个数为dp[i]
        dp[0]=1
        dp[1]=1
        dp[2]=2
        dp[3]=5
        2.
        dp[i] =
        for 1              2            3
         d[0]*dp[2]+dp[1]*dp[1]+dp[2]*dp[0]
        '''
        if n==0:
            return 1
        if n==1:
            return 1
        if n==2:
            return 2
        dp= [0] * (n+1)
        dp[0]=1
        dp[1]=1
        dp[2]=2
        for i in range(3, n+1, 1):
            for j in range(0, i, 1):
                dp[i] = dp[i] + dp[j]*dp[i-j-1]
        return dp[n]
        
# @lc code=end

