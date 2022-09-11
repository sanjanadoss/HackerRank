#https://leetcode.com/problems/reverse-linked-list/

def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    cur, prev = head, None
    while cur:
        #what actually happened in this case is all the right side of our assignment 
        #first gets copied to temorary vaiables and then they are assigned to left side
        cur.next, prev, cur = prev, cur, cur.next 
    return prev