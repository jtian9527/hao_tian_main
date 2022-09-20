class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1.异常流判断
        if len(nums) < 4:
            return []
        if len(nums) == 4:
            if nums[0]+nums[1]+nums[2]+nums[3] == target:
                return [nums]
        # 从小到大排序
        nums.sort()
        result = []
        for k in range(0, len(nums) - 3):
            # 值一样，直接跳过
            # if k > 0 and nums[k] == nums[k - 1]:
            #     continue
            for i in range(k+1, len(nums) - 1):
                # if nums[i] == nums[i - 1]:
                #     continue
                r = i + 1
                l = len(nums) - 1
                while r < l:
                    s = nums[k] + nums[i] + nums[r] +nums[l]
                    if s < target:
                        r = r + 1
                        # while r < l and nums[r] == nums[r - 1]:
                        #     r = r + 1
                    elif s > target:
                        l = l - 1
                        # while r < l and nums[l] == nums[l + 1]:
                        #     l = l - 1
                    else:
                        tmp = [nums[k], nums[i], nums[r], nums[l]]
                        if tmp not in result:
                            result.append([nums[k], nums[i], nums[r], nums[l]])
                        r = r + 1
                        l = l - 1
                        # while r < l and nums[r] == nums[r - 1]:
                        #     r = r + 1
                        # while r < l and nums[l] == nums[l + 1]:
                        #     l = l - 1
        return result

if __name__ == '__main__':
    nums = [0,-1,-3,5,-5]
    target = 1
    solution = Solution()
    print(solution.fourSum(nums,target))