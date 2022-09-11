#https://leetcode.com/problems/merge-sorted-array/discuss/?currentPage=1&orderBy=most_votes&query=


       #Adding elements to nums1 from the back
        last = m+n-1
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

#edge case where we just append the remaining elements in num2, to the beginning of nums1 since all the bigger elements were already added at the end. 
        while n>0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1