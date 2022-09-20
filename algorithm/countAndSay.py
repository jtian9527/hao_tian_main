class Solution:
    def countAndSay(self, n):
        #和斐波那契数列比较类似，求n个s字符串需要分析n-1
        if n == 1 :return "1"
        if n == 2 :return "11"
        prev = "1"
        for i in range(n-1):
            curr=""
            pos=0
            start=0
            while pos <len(prev):
                while pos < len(prev) and prev[pos] == prev[start]:
                    pos +=1
                curr += str(pos-start) + prev[start]
                start =pos
            prev = curr
        return prev

if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.countAndSay(n))