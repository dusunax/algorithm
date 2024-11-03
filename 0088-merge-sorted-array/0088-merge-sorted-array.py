class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n is 0:
            return
        p1, p2, index = m-1, n-1, m+n-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[index] = nums1[p1]
                p1 -= 1
            else:
                nums1[index] = nums2[p2]
                p2 -= 1
            index -= 1
        
        while p2 >= 0:
            nums1[index] = nums2[p2]
            index -= 1
            p2 -= 1
        
                