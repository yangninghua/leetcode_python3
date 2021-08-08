# @before-stub-for-debug-begin
from python3problem113 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (62.43%)
# Likes:    545
# Dislikes: 0
# Total Accepted:    160.7K
# Total Submissions: 256.9K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 
# 叶子节点 是指没有子节点的节点。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1,2], targetSum = 0
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点总数在范围 [0, 5000] 内
# -1000 
# -1000 
# 
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:

    def pr_dfs(self, node, path, cur_path_val, node_stack, targetSum):
        if not node:
            return
        cur_path_val += node.val
        node_stack.append(node.val)

        if (not node.left) and (not node.right) and (cur_path_val==targetSum):
            path.append(copy.deepcopy(node_stack))

        self.pr_dfs(node.left, path, cur_path_val, node_stack, targetSum)

        self.pr_dfs(node.right, path, cur_path_val, node_stack, targetSum)

        cur_path_val -= node.val
        node_stack.pop(-1)

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        # path = []
        # cur_path_val = 0
        # node_stack = []
        # self.pr_dfs(root, path, cur_path_val, node_stack, targetSum)
        # return path

        if not root:
            return []
        res = []
        # 栈 append pop(-1)
        stack = []
        stack.append((root,[root.val]))
        while stack:
            cur_node, cur_list = stack.pop(-1)
            
            if (not cur_node.left) and (not cur_node.right) and (sum(cur_list)==targetSum):
                res.append(cur_list)
            
            if cur_node.left:
                stack.append( (cur_node.left, cur_list+[cur_node.left.val]))
            
            if cur_node.right:
                stack.append((cur_node.right, cur_list+[cur_node.right.val]))
        
        return res


# @lc code=end

