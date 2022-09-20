class Solution:
    def permute(self, nums):
        # 找所有情况用回溯算法
        def func_permute(first):
            # 首先找退出条件
            if first == n:
                if nums[:] not in res:
                    res.append(nums[:])
            # 分析条件
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                func_permute(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        res = []
        n = len(nums)
        func_permute(first=0)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # solution = Solution()
    # print(solution.permute(nums))
    nums2 = str(nums)
    print(nums2 == [1,2,3,4])
