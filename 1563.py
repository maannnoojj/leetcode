from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)

        for i, x in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + x

        # dp[l][r] = maximum score Alice can obtain from l..r
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                left = 0
                right = prefix[r + 1] - prefix[l]
                best = 0

                for k in range(l, r):
                    left += stoneValue[k]
                    right -= stoneValue[k]

                    if left < right:
                        if best >= 2 * left:
                            continue

                        best = max(best, left + dp[l][k])

                    elif left > right:
                        if best >= 2 * right:
                            break

                        best = max(best, right + dp[k + 1][r])

                    else:
                        best = max(
                            best,
                            left + dp[l][k],
                            right + dp[k + 1][r]
                        )

                dp[l][r] = best

        return dp[0][n - 1]
