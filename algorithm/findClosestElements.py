class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # 首先找到最接近的那个数，然后向左向右双指针添加值
        # 向左向右每轮一位
        target_index = self.findMid(arr, x)
        r = target_index
        l = target_index - 1
        while k > 0:
            # 右边绝对值小一点，则该值进入比较，右边的index+1，反之左边的index - 1
            if r > len(arr) - 1:
                l = l - 1
            elif l < 0:
                r = r + 1
            elif x - arr[l] <= arr[r] - x:
                l = l - 1
            else:
                r = r + 1
            k = k - 1
        return arr[l+1:r]

    def findMid(self, arr, x):
        l = 0
        r = len(arr) - 1
        while l < r:
            # 向下取整的整数
            mid = int((r + l) / 2)
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    solution = Solution()
    print(solution.findClosestElements(arr, k, x))
