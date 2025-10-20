class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output =''
        carry = 0
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        elif len(a) > len(b):
            b = '0' * (len(a) - len(b)) +b
        for i in range(len(a)-1,-1,-1):
            c = int(a[i])+carry+int(b[i])
            output =  str(c%2) +output
            carry = c//2
        if carry > 0:
            output = '1'+output
        return output



if __name__ == '__main__':
    s = Solution()
    # print(s.addBinary("11","1"))
    print(s.addBinary("1010","1011"))