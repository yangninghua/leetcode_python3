# @before-stub-for-debug-begin
from python3problem136 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (71.65%)
# Likes:    1942
# Dislikes: 0
# Total Accepted:    452.5K
# Total Submissions: 630.3K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        # nums.sort()
        # for i in range(0, len(nums)-1, 2):
        #     if nums[i] != nums[i+1]:
        #         return nums[i]
        # return nums[-1]

        nums.sort()
        a = nums[0:len(nums):2]
        b = nums[1:len(nums):2]
        c = set(a)-set(b)
        return list(c)[0]

# @lc code=end

