class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.strip()
        c = len(a)
        b = []
        for i in range(c-1):
            if a[i] == ' ':
                b.append(i)
        if b : return c-b[-1] - 1
        else:
            return c
    def lengthOfLastWord2(self, s: str) -> int:
        end = len(s) - 1
        while s[end] == ' ':
            end -= 1
        start = end
        while s[start] != ' ' and start >= 0:
            start -= 1
        return end - start


if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLastWord2("hello world"))
    # print(s.lengthOfLastWord2("   fly me   to   the moon  "))
    print(s.lengthOfLastWord2("world"))