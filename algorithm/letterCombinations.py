class Solution:
    def letterCombinations(self, digits):
        # 拆分输入输入digits
        leng = len(digits)
        if leng == 0: return []
        res = []
        self.dfs(res, digits, "")
        return res

    def dfs(self, res, digits, path):
        # 创建dict存储数据
        digits_map_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        if len(digits) == 0:
            res.append(path)
            return
        tmp = digits[0]
        array = digits_map_dict[tmp]
        for item in array:
            self.dfs(res, digits[1:], path + item)


if __name__ == '__main__':
    digits = "23"
    solution = Solution()
    print(solution.letterCombinations(digits))
