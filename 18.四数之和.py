#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (40.39%)
# Likes:    918
# Dislikes: 0
# Total Accepted:    204.4K
# Total Submissions: 506.1K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a],
# nums[b], nums[c], nums[d]] ：
# 
# 
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# 你可以按 任意顺序 返回答案 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        for m_ind in range(0, len(nums), 1):

            if m_ind>0 and nums[m_ind]==nums[m_ind-1]:
                continue

            for n_ind in range(m_ind+1, len(nums), 1):

                if n_ind>m_ind+1 and nums[n_ind]==nums[n_ind-1]:
                    continue
                    
                left = n_ind + 1
                right = len(nums) - 1

                while left < right:
                    sum = nums[m_ind] + nums[n_ind] + nums[left] + nums[right]
                    if sum > target:
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        res.append([nums[m_ind] , nums[n_ind] , nums[left] , nums[right]])
                        

                        while (left < right) and nums[right]==nums[right-1]:
                            right -= 1
                        while (left < right) and nums[left]==nums[left+1]:
                            left += 1

                        left += 1
                        right -= 1
        return res
# @lc code=end

