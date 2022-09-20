# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #暴力解法
        leng = len(s)
        start = 0
        max_length = 1
        if len(s) < 2:
            return s
        for i in range(leng):
            for j in range(i+1,leng):
                if j-i+1>max_length and vaildPalindrome(s,i,j):
                    max_length = j-i+1
                    start = i
        result=""
        print(max_length)
        print(start)
        for i in range(max_length):
            result = result+s[start+i]
        return result


    def vaildPalindrome(self,s,i,j):
        while i<j:
            if s[i] != s[j]:
                return False
            i = i +1
            j = j -1
        return True

if __name__ == '__main__':
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome(s))
