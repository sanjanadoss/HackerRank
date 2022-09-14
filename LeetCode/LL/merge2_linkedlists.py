#https://leetcode.com/problems/merge-two-sorted-lists/
def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = cur = ListNode(-1) #only 1 extra node, not a whole new linked list, acts like dummy head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        #it depends on l1 or l2, which is not till the end of the linked list. 
        #if one of them is at the end(means None), then the other one will append to the result directly.
        cur.next = l1 or l2
        return dummy.next


