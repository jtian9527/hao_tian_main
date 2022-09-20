class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = tmp = ListNode(None)
        array = []
        while head:
            array.append(head.val)
            head = head.next
        leng = len(array)
        for i in range(leng):
            tmp.next = ListNode(array[leng-i-1])
            tmp = tmp.next
        tmp.next=None
        return res.next


if __name__ == '__main__':
    head = ListNode(1)
    Second = ListNode(3)
    Third = ListNode(2)
    head.next = Second
    Second.next = Third
    solution = Solution()
    print(solution.reverseList(head))