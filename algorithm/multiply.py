class Solution:
    def multiply(self, num1, num2):
        # 既然不能用乘法，那肯定是用加法，乘法是可以写成加法的
        if num1 == "0" or num2 == "0": return "0"
        # 两个字符串，转化成数组，然后每个元素去做处理
        sum = 0
        len_num1 = len(num1)
        len_num2 = len(num2)
        for i in range(len_num1):
            for j in range(len_num2):
                pos = 1
                num1_tmp = int(num1[i])
                num2_tmp = int(num2[j])
                all = len_num1-i-1 + len_num2-j-1
                for _ in range(all):
                    pos = 10 * pos
                sum = sum + num1_tmp * num2_tmp * pos

        return sum


if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    solution = Solution()
    print(solution.multiply(num1, num2))
