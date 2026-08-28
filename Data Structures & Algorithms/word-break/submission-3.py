class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        longest_word_length = 0

        for word in word_set:
            longest_word_length = max(longest_word_length, len(word))

        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return True
            
            for end in range(start, min(len(s), start + longest_word_length)):
                if s[start:end + 1] in word_set:
                    if dfs(end + 1):
                        memo[start] = True
                        return True
                    
            memo[start] = False
            return False

        return dfs(0)