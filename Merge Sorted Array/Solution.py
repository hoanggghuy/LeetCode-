from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a = m - 1
        b = n - 1
        right = m + n - 1
        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[right] = nums1[a]
                a -= 1
            else:
                nums1[right] = nums2[b]
                b -= 1
            right -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.merge([0,0,0,0,0],0,[1,2,3,4,5],5))