class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        output = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return output
            output+= first[i]
        return output
    def longestCommonPrefix2(self, strs: list[str]) -> str:
        output = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return output
            output += strs[0][i]
        return output




if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix2(["flower","flow","flight"]))
    print(s.longestCommonPrefix2(["dog","racecar","car"]))
    print(s.longestCommonPrefix2([""]))