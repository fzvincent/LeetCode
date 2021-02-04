def findMedianSortedArrays(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    a = m + n
    if a % 2 == 0:
        b = a / 2 - 1
    else:
        b = a // 2
    while b != 0:
        if nums1:
            if nums2:
                if nums1[0]<nums2[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
            else:#
                if a%2==0:
                    return((nums1[int(len(nums1)/2)]+nums1[int(len(nums1)/2-1)])/2)
                else:
                    return (nums1[len(nums1)//2])
        else:
            if a % 2 == 0:
                return ((nums2[int(len(nums2)/2)] + nums2[int(len(nums2)/2 - 1)]) / 2)
            else:
                return (nums2[len(nums2) // 2])
        if nums1:
            if nums2:
                if nums1[-1]<nums2[-1]:
                    nums2.pop()
                else:
                    nums1.pop()
            else:
                nums1.pop()
        else:
            nums2.pop()
        b=b-1
    return ((sum(nums1) + sum(nums2)) / (len(nums1) + len(nums2)))
nums1=[3,4,5,6,7,8]
nums2=[1,2]
print(findMedianSortedArrays(nums1,nums2))