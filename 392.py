def isSubsequence( s: str, t: str) -> bool:
    def rec(s, t):
        if s == None:
            return True

    for i in range(len(t)):
        if s[0] == t[i]:
            return rec(s[1:], t[i + 1:])
        if i == len(t) - 1:
            return False
s = "abc"
t = "ahbgdc"
isSubsequence(s,t)
