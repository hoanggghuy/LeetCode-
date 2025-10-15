class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1









if __name__ == '__main__':
    s = Solution()
    print(s.strStr("hello", "ll"))
    print(s.strStr("sad", "sad"))
    print(s.strStr("leetcode", "leeto"))
    print(s.strStr("abc", "c"))