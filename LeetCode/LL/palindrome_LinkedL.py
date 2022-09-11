#https://leetcode.com/problems/palindrome-linked-list/

def isPalindrome(self, head):
    """
    O(n) time and O(1) space so check inside
    Linked List itself// no reasigning
    """

    fast = slow = head

    #even and odd nodes condition
    #find mid(slow gives it)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #reverse the LL from end
    cur, prev = slow, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next

    #check if nodes are the same
    l, r = head, prev
    while r:
        if l.val != r.val:
            return False
        l = l.next
        r = r.next
    return True

#array solution with O(n) space
def isPalindromeArrsol(self, head):
    nums = []

    while head:
        nums.append(head.val)
        head = head.next

    l, r=0, len(nums)-1
    while l<=r:
        if nums[l] != nums[r]:
            return False
        l += 1
        r -= 1
    return True