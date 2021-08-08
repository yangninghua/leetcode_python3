# @before-stub-for-debug-begin
from python3problem236 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (67.50%)
# Likes:    1237
# Dislikes: 0
# Total Accepted:    231.5K
# Total Submissions: 341.7K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [2, 10^5] 内。
# -10^9 
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import copy
class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node,target,path): # dfs递归
            if not node: return # 到底了返回
            if node == target:  # 到了目标节点
                path.append(node) # 放到list里面
                return target
            val = dfs(node.left,target,path) # 递归左分支
            if val: 
                path.append(node) # 如果左分支返回了值，说明当前节点是目标节点的父节点
                return node
            val = dfs(node.right,target,path) # 递归右边
            if val: 
                path.append(node)
                return node

        path_p, path_q = [], []
        dfs(root, p, path_p) # 查找p的路径
        dfs(root, q, path_q) # 查找q的路径

        #print(path_p)
        if not path_p: return p # 如果p路径为空，说明p是起点，直接返回p
        if not path_q: return q # 如果q路径为空，说明q是起点，直接返回q
        for item in path_p: # 找到p和q的公共节点
            if item in path_q:
                return item

        return None


    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if not root or root == p or root == q:
    #         return root
        
    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)
        
    #     # 左右子树都为空
    #     if not left and not right:
    #         return None
    #     # 右子树为空
    #     elif left and not right:
    #         return left
    #     # 左子树为空
    #     elif not left and right:
    #         return right
    #     # 左右子树都不为空
    #     return root


        
# @lc code=end

