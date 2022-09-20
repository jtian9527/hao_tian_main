class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 首先把当前结点初始化为返回列表的哑节点
        res = temp = ListNode(None)
        # 进位0
        add = 0
        # 如果存在值
        while l1 or l2 or add:
            add += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            temp.next = ListNode(add % 10)
            add //= 10
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))
