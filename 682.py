# coding: utf-8
'''
682. 棒球比赛

给定一个字符串列表，每个字符串可以是以下四种类型之一：
1.整数（一轮的得分）：直接表示您在本轮中获得的积分数。
2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。
3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。
4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。

栈的基本实现
'''


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for item in ops:
            if item == "C":
                stack.pop()
            elif item == "D":
                stack.append(stack[-1] * 2)
            elif item == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(item))
        return sum(stack)


if __name__ == '__main__':
    s = Solution()
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(s.calPoints(ops))
