class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid
            elif mid * mid == x:
                return mid
            if right - left == 1 :
                return left



if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(8))
    print(s.mySqrt(4))
    print(s.mySqrt(5))
    print(s.mySqrt(2))