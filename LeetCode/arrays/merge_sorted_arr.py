#https://leetcode.com/problems/merge-sorted-array/
def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a, b, trav_p = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]: 
                nums1[trav_p] = nums1[a]
                a -= 1
            else: #handles edge case where there are remaining elements 
                #in b and they just have to be appended in a
                nums1[trav_p] = nums2[b]
                b -= 1

            trav_p -= 1
