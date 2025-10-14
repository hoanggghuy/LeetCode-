class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l = 0
        r = len(nums)-1
        if val not in nums: return len(nums)
        while l < r:
            if nums[l] == val:
                if nums[r] == val:
                    r -= 1

                else:
                    nums[l] = nums[r]
                    nums[r] = val
                    l+=1
            else:
                l+=1
            continue
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], 3))
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))