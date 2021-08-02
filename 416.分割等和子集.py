# @before-stub-for-debug-begin
from python3problem416 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (50.30%)
# Likes:    873
# Dislikes: 0
# Total Accepted:    150.5K
# Total Submissions: 298.4K
# Testcase Example:  '[1,5,11,5]'
#
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
        集合中能否出现总和为sum/2的子集
        1. dp[i]表示 背包总容量是i，最⼤可以凑成i的⼦集总和为dp[i]
        '''
        sum_num = sum(nums)
        if sum_num % 2 == 1:
            return False
        target = sum_num//2
        dp = [0] * (target+1)

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
                
        print(dp)
        if dp[target]==target:
            return True
        return False

        

# @lc code=end

