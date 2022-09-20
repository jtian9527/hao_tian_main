class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_list = []
        while head:
            if len(node_list)==0:
                node_list.append(head.val)
            else:
                #直接在这里排序,node_list已经是顺序数组
                for i in range(len(node_list)):
                    if head.val <= node_list[i]:
                        #原来第i个位置的前面
                        node_list.insert(i,head.val)
                        break
                    #最后一个位置还没找到
                    if i == (len(node_list)-1):
                        node_list.append(head.val)
                        break
            head = head.next
        re = tmp = ListNode(None)
        for j in range(len(node_list)):
            tmp.next = ListNode(node_list[j])
            tmp = tmp.next
        return re.next

if __name__ == '__main__':
    head = ListNode(4)
    Second = ListNode(2)
    Third = ListNode(1)
    head.next = Second
    Second.next = Third
    solution = Solution()
    print(solution.sortList(head))