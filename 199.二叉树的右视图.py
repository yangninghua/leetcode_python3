# @before-stub-for-debug-begin
from python3problem199 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (64.93%)
# Likes:    513
# Dislikes: 0
# Total Accepted:    126K
# Total Submissions: 193.6K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
# 
# 
# 示例 2:
# 
# 
# 输入: [1,null,3]
# 输出: [1,3]
# 
# 
# 示例 3:
# 
# 
# 输入: []
# 输出: []
# 
# 
# 
# 
# 提示:
# 
# 
# 二叉树的节点个数的范围是 [0,100]
# -100  
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
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:



    def BFS_1(self, root, val_list):
        queue=[]#模拟队列
        if not root:
            return []
        queue.append(root)

        while len(queue):
            level=[]#记录当前层的节点值
            size=len(queue)
            for _ in range(size):              
                current_node = queue.pop(0)
                level.append(current_node.val)
                '''判断该节点是否有左孩子，有就入队'''
                if current_node.left:
                    queue.append(current_node.left)
                '''判断该节点是否有右孩子，有就入队'''
                if current_node.right:
                    queue.append(current_node.right)
            if level:
                val_list.append(level)
        return val_list


    def BFS_2(self, root, val_list):
        '''
        广度优先遍历，即从上到下，从左到右遍历。
        主要利用队列先进先出的特性，入队的时候，是按根左右的顺序，那么只要按照这个顺序出队就可以了
        '''
 
        if root == None:
            return None
        queue = []
        '''用列表模仿入队'''
        queue.append(root)
        
        while queue:
            '''将队首元素出栈'''
            current_node = queue.pop(0)
            val_list.append(current_node.val)
            '''判断该节点是否有左孩子，有就入队'''
            if current_node.left:
                queue.append(current_node.left)
            '''判断该节点是否有右孩子，有就入队'''
            if current_node.right:
                queue.append(current_node.right)

    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        val_list = []
        self.BFS_1(root, val_list)
        res = []
        for m in val_list:
            res.append(m[-1])
        return res


# @lc code=end

