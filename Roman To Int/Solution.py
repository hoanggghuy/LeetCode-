class Solution:
    def romanToInt(self, s: str) -> int:
        dict_num = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 }
        s = s + "0"
        len_s = len(s)
        output = 0
        for i in range(len_s-1):
            if s[i] in dict_num and s[i+1] in dict_num:
                a = dict_num[s[i]]
                b = dict_num[s[i+1]]
            if a >= b:
                output += a
            else:
                output -= a

        return output
    def romanToInt2(self, s: str) -> int:
        dict_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        len_s = len(s)
        output = 0
        for i in range(len_s):
            a =dict_num[s[i]]
            b = dict_num[s[i+1]] if i < len_s - 1 else 0
            if a >= b:
                output += a
            else:
                output -= a
        return output

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt2("III"))
    print(s.romanToInt2("IV"))