class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return n
        re = 1
        last_index = 0
        last_two_index = 0
        for _ in range(2, n+1):
            last_two_index = last_index
            last_index = re
            re = last_index + last_two_index
        return re


if __name__ == '__main__':
    n = 5
    solution = Solution()
    print(solution.fib(n))
