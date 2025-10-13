class Solution:
    def removeDuplicates(self, nums: list[int]) :
        k = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] != nums[j] and nums[i]<= nums[j]:
                    nums[i+1] = nums[j]
                    break
                elif nums[i] == nums[j] :
                    continue
            k += 1
            if nums[i] == nums[-1]:
                break
        return nums,k
    def removeDuplicates2(self, nums: list[int]) :
        l=1
        r=1
        if not nums :
            return 0
        while r < len(nums) :
            if nums[l] < nums[r]:
                nums[l+1] = nums[r]
                l+=1
                r+=1
            else:
                r +=1
        return nums,l
    def removeDuplicates3(self, nums: list[int]) :
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[l-1]:
                nums[l] = nums[r]
                l+=1
        return l,nums



if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates2([1,1,2]))
    print(s.removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))
