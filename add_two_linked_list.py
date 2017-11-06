# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
        current = l1
        while current != None:
            print(current.val)
            current = current.next
    """
        
    def remai(self,val):
        if val>=10:
            return val%10
        else:
            return val
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        src1=l1
        src2=l2
        res=temp=ListNode((src1.val+src2.val)%10)
        count=int((src1.val+src2.val)/10)
        while(src1.next or src2.next or count!=0):
            src1=src1.next or ListNode(0)
            src2=src2.next or ListNode(0)
            temp.next=ListNode(self.remai((src1.val+src2.val)%10+count))
            temp=temp.next
            count=int((src1.val+src2.val+count)/10)
        return res
        
