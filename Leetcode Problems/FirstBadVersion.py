# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        ans = []
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2

            if isBadVersion(mid):
                ans.append(mid)
                r = mid - 1
            else:
                l = mid + 1
        return min(ans)




