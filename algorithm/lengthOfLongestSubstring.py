class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 思路：从第一个字母开始，宽度为1，开始滑动，直至字符终点
        # 滑动规则：right+1，然后判断right是否属于[left:right]字符
        # 如果不属于，right继续+1，now_len = right - left,max 与 now比较，now大于则，max=now
        # 如果属于，left+1，继续比较right是否属于[left:right]字符，直到不属于为止
        # 重复此操作，便利完成，返回max
        max_len = 1
        left_index = 0
        right_index = 0
        now_len = 0
        str_len = len(s)
        if s == "": return 0
        if len(s) == 1: return 1

        for i in range(str_len):
            if s[right_index] not in s[left_index:right_index] or left_index == right_index:
                now_len = right_index - left_index + 1
                right_index = right_index + 1
            else:
                copy_index = s[left_index:right_index].find(s[right_index])
                left_index = left_index + 1 + copy_index
                right_index = right_index + 1
            if now_len > max_len:
                max_len = now_len
        return max_len


if __name__ == '__main__':
    s = "ab"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
