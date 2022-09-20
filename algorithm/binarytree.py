class Solution(object):
    result_list = []

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def mid_order(self):
        pass


if __name__ == '__main__':
    a = Solution()
    b = Solution()
    c = Solution()
    a.value = "1"
    b.value = "2"
    c.value = "3"
    a.left = b
    a.right = c
    print(a.left.value)
