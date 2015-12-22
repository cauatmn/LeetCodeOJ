# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two #numbers and return it as a linked list.
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Subscribe to see which companies asked this question
#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
		
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy,flag = ListNode(0),0
        head = dummy
        while flag or l1 or l2:
            node = ListNode(flag)
            if l1:
                node.val +=l1.val
                l1 = l1.next
            if l2:
                node.val +=l2.val
                l2 = l2.next
            flag = node.val / 10 
            node.val %= 10
            head.next = node
            head = head.next			
        return dummy.next
		
if __name__ == '__main__':
	L1 = [0]
	L2 = [0]
	Test = Solution()
	output = Test.addTwoNumbers(L1,L2)
	