class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            sum = target - num
            if (sum in nums) and (sum != num) :
                return [i,nums.index(sum)]
            elif (sum in nums) and (i != nums.index(sum)) :
                return [nums.index(sum),i]
            else: None

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        dict_num = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in dict_num: return[dict_num[a], i]
            else : dict_num[nums[i]] = i



if __name__ == '__main__':
    s = Solution()
    print(s.twoSum2([2,3,3,9], 6))
    print(s.twoSum2([2,7,11,15], 9))

"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
111111
"""
