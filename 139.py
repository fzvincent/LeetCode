s = "leetcode"
wordDict = ["leet", "cod"]



def wordBreak( s, wordDict) :

#--------------------------------------------------------------------------------
    #         return self.helper(s, {len(i) for i in wordDict}, set(wordDict), set())
    #     def helper(self, s, ranges, words, memo):
    #         if s=="":
    #             return True
    #         elif s in memo:
    #             return False
    #         memo.add(s)
    #         return any(self.helper(s[i:], ranges, words, memo) for i in ranges if s[:i] in words)
#--------------------------------------------------------------------------------

    def helper(s, ranges, words, memo):
        if not words:
            return True
        elif s in memo:
            return False
        memo.add(s)

        #return any(helper(s[i:], ranges, words, memo) for i in ranges if s[:i] in words)
        for i in ranges:
            if s[:i] in words:
                a=s[:i]
                words.remove(a)
                return helper(s[i:], ranges, words, memo)


    return helper(s, {len(i) for i in wordDict}, set(wordDict), set())

print(wordBreak(s,wordDict))