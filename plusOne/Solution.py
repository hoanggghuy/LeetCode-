class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = 0
        for num in digits:
            a = a*10 + num
        a = a+1
        output = []
        while a!= 0 :
            c = a % 10
            output.append(c)
            a = a //10
        return output[::-1]
    def plusOne2(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            digits[i] = 0
            if i == 0:
                return [1] + digits




if __name__ == '__main__':
    s = Solution()
    print(s.plusOne2([1,2,3]))
    print(s.plusOne2([5,9]))