# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 9:08
# @Author  : GuYi
# @Function    : 844. 比较含退格的字符串


"""
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，请你判断二者是否相等。# 代表退格字符。

如果相等，返回 true ；否则，返回 false 。

注意：如果对空文本输入退格字符，文本继续为空。

输入：s = "ab#c", t = "ad#c"
 a b # c -> a c
 a d # c -> a c
输出：true
解释：S 和 T 都会变成 “ac”。

输入：s = "a#c", t = "b"
a # c -> c
b
输出：false
解释：s 会变成 “c”，但 t 仍然是 “b”。

"""


# 栈
# str3 = "ab##"
# str4 = "c#d#"
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = []
        new_t = []
        for i in range(len(s)):
            if s[i] != "#":
                new_s.append(s[i])
            elif s[i] == "#" and new_s != []:
                new_s.pop()
        for i in range(len(t)):
            if t[i] != "#":
                new_t.append(t[i])
            elif t[i] == "#" and new_t != []:
                new_t.pop()
        return new_s == new_t

# 双指针
class Solution1:
    def backspaceCompare(self, s: str, t: str) -> bool:
        counter_t , counter_s = 0
        # 从后往前遍历
        for i in range(len(s) - 1, -1, -1),range(len(t) - 1, -1, -1):
            while i >= 0:
                if s[i] == "#":
                    counter_s += 1
                    i -= 1
                elif counter_s > 0:
                    counter_s -= 1
                    i -= 1


if __name__ == '__main__':
    str1 = "ab#c"
    str2 = "ad#c"
    str3 = "ab##"
    str4 = "c#d#"
    solution = Solution()
    # print(solution.backspaceCompare(str1, str2))
    print(solution.backspaceCompare(str3, str4))
