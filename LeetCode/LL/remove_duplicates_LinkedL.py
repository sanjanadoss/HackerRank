def removeElements(self, head, val):
        """
        edge cases:
        .The linked list is empty, i.e. the head node is None.
        .Multiple nodes with the target value in a row.
        .The head node has the target value.
        .The head node, and any number of nodes immediately after it have the target value.
        .All of the nodes have the target value.
        .The last node has the target value.
        
        The algorithm requires O(1) extra space and takes O(n) time.
        """
        
        dummy = ListNode(-1)
        dummy.next = head
        
        counter = dummy
        while counter.next != None:
            if counter.next.val == val:
                counter.next = counter.next.next
            else:
                counter = counter.next
                
        return dummy.next