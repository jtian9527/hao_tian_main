class Solution:
    def maxArea(self, height):
        #两条线i,j的面积为 s = (j-i) * min(height[i],height[j])
        #从两边开始，具体从左还是从右收缩，得看左右哪个高，从矮的收缩，一样则随意
        #因为从高的收缩面积一定变小，因为 (j-i) & min(height[i],height[j])都会变小

        L = 0
        R = len(height) - 1
        max_area = 0
        if len(height) <= 1 : return 0
        while L<R:
            now_area = (R-L) * min(height[R],height[L])
            max_area = max(max_area,now_area)
            if height[R]>=height[L]:
                L = L + 1
            else:
                R = R - 1
        return max_area

if __name__ == '__main__':
    # height = [1,8,6,2,5,4,8,3,7]
    # solution = Solution()
    # print(solution.maxArea(height))
    x = ["a","b"]
    y = ["c","d"]
    print(x*y)
