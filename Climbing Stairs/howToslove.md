# 🧠 Intuition

This problem asks us to find the number of distinct ways to climb to the top of a staircase with `n` steps, where we can either take **1 step** or **2 steps** at a time.

To solve this, we realize that:
- The total number of ways to reach step `n` is the sum of the number of ways to reach `n-1` and `n-2`.
- Why? Because from step `n-1`, we can take a 1-step to reach `n`; from step `n-2`, we can take a 2-step to reach `n`.

Thus, the recurrence becomes:
ways(n) = ways(n-1) + ways(n-2)


This resembles the Fibonacci sequence and can be solved using recursion. However, plain recursion leads to redundant calculations. So we use **memoization** to store the result of each subproblem and avoid recomputation.

---

# 🚀 How to Solve

1. Create a list `dp` of size `n` initialized with `-1` to store results for each step.
2. Define a recursive function `traverse(step)` that returns the number of ways to reach the top from the current `step`.
3. Base cases:
   - If `step == n`: we've reached exactly the top → return 1.
   - If `step > n`: overshot the staircase → return 0.
4. If `dp[step] != -1`, we've already calculated the answer → return it.
5. Otherwise:
   - Calculate the result by calling `traverse(step + 1)` and `traverse(step + 2)`.
   - Store the result in `dp[step]`.
6. Finally, call `traverse(0)` and return `dp[0]`.

---

# ✅ Code

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        
        def traverse(step):
            if step == n:
                return 1
            elif step > n:
                return 0
            if dp[step] != -1:
                return dp[step]

            x = traverse(step + 1)
            y = traverse(step + 2)
            dp[step] = x + y
            return dp[step]
        
        traverse(0)
        return dp[0]
```

⏱️ Time and Space Complexity
Time Complexity:
$O(n)$
Each step from 0 to n is computed only once due to memoization.

Space Complexity:
$O(n)$

For the dp list.

Call stack of recursion can go up to n depth.
