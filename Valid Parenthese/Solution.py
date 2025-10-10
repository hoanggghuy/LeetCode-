class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(","[","{"]
        close = [")","]","}"]
        dict = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        list1 =[]
        list2 =[]
        for i in range(len(s)):
            if s[i] in open:
                list1.append(s[i])
            if s[i] in close:
                list2.append(s[i])
        if len(list1) != len(list2): return False
        if len(s) % 2 == 1: return False
        if s[0] in close or (s[0] in open and s[len(s)-1] in open): return False
        for i in range(len(s)):
            if s[i] in open:
                stack.append(s[i])
            if s[i] in close:
                if dict[s[i]] != stack.pop():
                    return False
        if len(stack) == 0: return True


    def isValid2(self, s: str) -> bool:
        stack = []
        close2open = {")": "(", "]": "[", "}" : "{"}
        for char in s:
            if char in close2open:
                if stack and stack[-1] == close2open[char]:
                    stack.pop()
                else:
                    return False
            else :
                stack.append(char)
        return True if not stack else False









if __name__ == "__main__":
    s = Solution()
    print(s.isValid2("()[]{}"))
    print(s.isValid2("(]"))
    print(s.isValid2("([)]"))
    print(s.isValid2("(){}}{"))
    print(s.isValid2("{}{}{}{}{}{(([[]]))]"))
