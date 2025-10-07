class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        b = a[::-1]
        if b == a : return True
        else: return False

    def isPalindrome2(self, x: int) -> bool:
        if x < 0 : return False
        div = 1
        while x >= 10*div:
            div *= 10
        while x:
            left = x // div
            right = x%10
            if left != right: return False
            x = (x%div)//10
            div = div /100
        return True
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome2(0))


"""
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""