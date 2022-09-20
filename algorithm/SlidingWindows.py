# -*- coding: utf-8 -*-
from collections import deque

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        index = 0
        # 因为这里需要从窗口的两端进行元素的增加或减少，因此采用双端队列
        slide_win = deque()
        # 题目要求最长子串长度，因此需要在滑动过程中更新最大长度
        max_len = 0
        while index < len(s):
            ch = s[index]
            # 如果当前元素不在窗口中，则加入窗口
            if ch not in slide_win:
                slide_win.append(ch)
                # 窗口的右端向前滑动，左端不变（扩大窗口）
                index += 1
            else:
                # 当前元素已经存在窗口中，即表示找到一个可行解，更新最大长度
                max_len = max(max_len, len(slide_win))
                # 将窗口中在当前元素值之前的元素全部移除掉，即窗口左端向前滑动，右端不变（缩小窗口）
                while ch in slide_win:
                    slide_win.popleft()
        return max(max_len, len(slide_win))

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = 0
        self.maxsize = size
        self.stack = deque([])
        self.sum = 0


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.size < self.maxsize:
            #小于窗口时，直接往队列里添加值
            self.size += 1
            self.stack.append(val)
            self.sum += val
        else:
            #大于等于窗口时，需要从sum中去掉最先进队列的数，然后再加上新进队列的数
            self.stack.append(val)
            self.sum -= self.stack.popleft()
            self.sum += val
        return round((self.sum / self.size), 5)

if __name__ == '__main__':
    # movingAverage = MovingAverage(3)
    # print(movingAverage.next(1))
    # print(movingAverage.next(10))
    # print(movingAverage.next(3))
    # print(movingAverage.next(5))
    a = [1,2,3]
    b=2
    print(a*b)

