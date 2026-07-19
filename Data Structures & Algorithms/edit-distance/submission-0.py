class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def helper(M, N):
            if (M, N) in memo:
                return memo[(M, N)]

            if M == len(word1):
                return len(word2) - N
            if N == len(word2):
                return len(word1) - M

            if word1[M] == word2[N]:
                memo[(M, N)] = helper(M + 1, N + 1)
            else:
                insert = helper(M, N + 1)
                delete = helper(M + 1, N)
                replace = helper(M + 1, N + 1)
                memo[(M, N)] = 1 + min(insert, delete, replace)

            return memo[(M, N)]

        return helper(0, 0)
