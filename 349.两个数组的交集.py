# @before-stub-for-debug-begin
from python3problem349 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (73.77%)
# Likes:    394
# Dislikes: 0
# Total Accepted:    199.6K
# Total Submissions: 270.6K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 
# 
# 示例 2：
# 
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 
# 
# 
# 说明：
# 
# 
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
# 
# 
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # a = set(nums1)
        # b = set(nums2)
        # c = a & b
        # return list(c)


        # result_set = set()
        # set1 = set(nums1)
        # for num in nums2:
        #     if num in set1:
        #         result_set.add(num) # set1里出现的nums2元素 存放到结果
        # return list(result_set)


        # res = []
        # for i in nums1:
        #     if i not in res and i in nums2:
        #         res.append(i)
        
        # return res


        # 排序后 定位 双指针
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if nums1[i] not in res:
                    res.append(nums1[i])
                # if not (len(res) and nums1[i] == res[len(res)-1]):
                #     res.append(nums1[i])
                i += 1
                j += 1
        
        return res

# @lc code=end

