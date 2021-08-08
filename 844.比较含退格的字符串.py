#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#
# https://leetcode-cn.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (51.75%)
# Likes:    296
# Dislikes: 0
# Total Accepted:    80.1K
# Total Submissions: 154.8K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
# 
# 注意：如果对空文本输入退格字符，文本继续为空。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
# 
# 
# 示例 2：
# 
# 
# 输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S 和 T 都会变成 “”。
# 
# 
# 示例 3：
# 
# 
# 输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S 和 T 都会变成 “c”。
# 
# 
# 示例 4：
# 
# 
# 输入：S = "a#c", T = "b"
# 输出：false
# 解释：S 会变成 “c”，但 T 仍然是 “b”。
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# S 和 T 只含有小写字母以及字符 '#'。
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # s = list(s)
        # t = list(t)
        # size_s = len(s)
        # slow = 0
        # fast = 0
        # while fast < size_s:
        #     if s[fast] == '#':
        #         fast += 1
        #         slow -= 1
        #         if slow<0:
        #             slow=0
        #     elif s[fast] != '#':
        #         s[slow] = s[fast]
        #         fast += 1
        #         slow += 1
        # slow_s = slow

        # size_t = len(t)
        # slow = 0
        # fast = 0
        # while fast < size_t:
        #     if t[fast] == '#':
        #         fast += 1
        #         slow -= 1
        #         if slow<0:
        #             slow=0
        #     elif t[fast] != '#':
        #         t[slow] = t[fast]
        #         fast += 1
        #         slow += 1
        # slow_t = slow

        # if s[0:slow_s] == t[0:slow_t]:
        #     return True
        # else:
        #     return False


        s_temp, t_temp = [], []
        for i in s: 
            s_temp = s_temp + [i] if i != '#' else s_temp[:-1]
        for i in t: 
            t_temp = t_temp + [i] if i != '#' else t_temp[:-1]
        return s_temp == t_temp

# @lc code=end

