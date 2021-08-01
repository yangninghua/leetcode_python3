# @before-stub-for-debug-begin
from python3problem283 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (63.85%)
# Likes:    1150
# Dislikes: 0
# Total Accepted:    427.5K
# Total Submissions: 669.6K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if len(nums)==1:
        #     return
        # if sum(nums)==0:
        #     return

        # left = 0
        # right = 1
        # while right < len(nums) and left < len(nums):
        #     if nums[left]==0:
        #         if nums[right]!=0:
        #             nums[left], nums[right] = nums[right], nums[left]
        #             left += 1
        #             right += 1
        #         else:
        #             right += 1
        #     else:
        #         left += 1
        #         right += 1

        # for m in nums:
        #     if m ==0:
        #         nums.remove(0)
        #         nums.append(0)
        # return

        left = 0
        p_end = 0

        while p_end<len(nums):
            if nums[left]==0:
                nums[left:len(nums)-1] = nums[left+1:len(nums)]
                nums[-1] = 0
                p_end +=1
            else:
                left+=1
                p_end+=1
        return



# @lc code=end

