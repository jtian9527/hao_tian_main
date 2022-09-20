# -*- coding: utf-8 -*-
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        dict = {}
        for i, v in enumerate(words):
            if v in dict:
                dict[v] = dict[v] + 1
            else:
                dict[v] = 1

        # 根据value值进行快速排序,先取数组

        list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
        array = []
        for i in range(k):
            array.append(list[i][0])
        return array


if __name__ == '__main__':
    words = ["i","love","leetcode","i","love","coding"]
    k = 3
    solution = Solution()
    print(solution.topKFrequent(words, k))
    # a = [-1,10]
    # b = -1
    # print(b in a)
