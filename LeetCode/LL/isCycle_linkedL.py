#https://leetcode.com/problems/linked-list-cycle/

def hasCycle(self, head):
    """
    If there is a cycle, fast will catch slow after some loops.
    2 pointer approach
    use  slow.val ==fast.val for same values finding
    """
    
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False