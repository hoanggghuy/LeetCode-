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


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("hello world"))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord("world"))