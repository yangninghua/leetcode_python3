# @before-stub-for-debug-begin
from python3problem392 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#
# https://leetcode-cn.com/problems/is-subsequence/description/
#
# algorithms
# Easy (51.23%)
# Likes:    474
# Dislikes: 0
# Total Accepted:    132.8K
# Total Submissions: 259K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 
# 
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 
# 进阶：
# 
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T
# 的子序列。在这种情况下，你会怎样改变代码？
# 
# 致谢：
# 
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# 两个字符串都只由小写字符组成。
# 
# 
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # [行 for 列]
        dp = [ [0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(1, (len(s)+1), 1):
            for j in range(1, (len(t)+1), 1):
                #error if s[i]==t[j]:
                #dp数据和s t的访问不一致，要注意
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        if dp[len(s)][len(t)] == len(s):
            return True
        else:
            return False
# @lc code=end

