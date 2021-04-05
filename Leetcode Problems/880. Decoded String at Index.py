class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        N = len(S)
        size = 0

        # finding size = length of new string S'
        for i in range(0, N):
            if S[i].isdigit():
                size = size * int(S[i])
            else:
                size += 1

        # get the K-th letter
        for i in range(N - 1, -1, -1):
            K %= size

            if K == 0 and S[i].isalpha():
                return S[i]

            if S[i].isdigit():
                size = size // int(S[i])
            else:
                size -= 1