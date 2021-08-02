# @before-stub-for-debug-begin
from python3problem200 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (54.37%)
# Likes:    1233
# Dislikes: 0
# Total Accepted:    280K
# Total Submissions: 513.2K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 的值为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     # 深度优先搜索
    #     if not grid:
    #         return 0
    #     count = 0
    #     for m_ind, m_val in enumerate(grid):
    #         for n_ind, n_val in enumerate(grid[0]):
    #             if grid[m_ind][n_ind] == "1":
    #                 self.dfs(grid, m_ind, n_ind)
    #                 count += 1
    #     return count
    # def dfs(self, grid, m_ind, n_ind):
    #     # if m_ind<0 or n_ind<0 or m_ind>len(grid) or n_ind>len(grid[0]) or grid[m_ind][n_ind] != "1":
    #     #     return
    #     if m_ind<0 or n_ind<0 or m_ind>=len(grid) or n_ind>=len(grid[0]) or grid[m_ind][n_ind] != "1":
    #         return
    #     grid[m_ind][n_ind] = "#"
    #     self.dfs(grid, m_ind+1, n_ind)
    #     self.dfs(grid, m_ind-1, n_ind)
    #     self.dfs(grid, m_ind, n_ind+1)
    #     self.dfs(grid, m_ind, n_ind-1)

    # https://leetcode-cn.com/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/
    # bfs
    def numIslands(self, grid: List[List[str]]) -> int:
        # 深度优先搜索
        if not grid:
            return 0
        count = 0
        for m_ind, m_val in enumerate(grid):
            for n_ind, n_val in enumerate(grid[0]):
                if grid[m_ind][n_ind] == "1":
                    self.bfs(grid, m_ind, n_ind)
                    count += 1
        return count

    def bfs(self, grid, m_ind, n_ind):
        queue = []
        queue.append((m_ind,n_ind))
        while queue:
            #list.pop([index=-1])
            #list.pop(0)移除list第一个数据
            #list.pop() or list.pop(-1)移除list最后一个数据
            m_ind, n_ind = queue.pop(0)
            if 0<= m_ind < len(grid) and 0<= n_ind < len(grid[0]) and grid[m_ind][n_ind] == '1':
                grid[m_ind][n_ind] = "#"
                queue.append((m_ind-1, n_ind))
                queue.append((m_ind, n_ind+1))
                queue.append((m_ind, n_ind-1))
                queue.append((m_ind+1, n_ind))

# @lc code=end

