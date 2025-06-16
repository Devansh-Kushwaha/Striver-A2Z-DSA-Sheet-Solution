# 🧾 Line-by-Line Explanation: Climb Stairs (Recursive + Memoization)

```python
class Solution:
```
- Defines a class `Solution` that will contain our method.

```python
    def climbStairs(self, n: int) -> int:
```
- Defines the method `climbStairs` which takes the number of steps `n` as input and returns the number of distinct ways to reach the top.

```python
        ans = 0
```
- Initializes a variable `ans`. ⚠️ This line is **unused** and can be removed.

```python
        dp = [-1] * n
```
- Initializes a list `dp` of size `n` with all values set to `-1`.
- This list is used for **memoization** to store the number of ways to reach the top from each step.

```python
        def traverse(step):
```
- Declares a helper recursive function `traverse` that returns the number of ways to reach step `n` from the current `step`.

```python
            if step == n:
                return 1
```
- **Base case**: If we've reached exactly step `n`, that's one valid way → return 1.

```python
            elif step > n:
                return 0
```
- **Invalid case**: If we've gone past step `n`, it's not a valid path → return 0.

```python
            if dp[step] != -1:
                return dp[step]
```
- If we've already calculated the number of ways from this step, return the memoized value to avoid recomputation.

```python
            x = traverse(step + 1)
            y = traverse(step + 2)
```
- Recursively calculate the number of ways by taking:
  - 1 step forward (`step + 1`)
  - 2 steps forward (`step + 2`)

```python
            dp[step] = x + y
```
- Store the total number of ways from the current step in the memoization array.

```python
            return x + y
```
- Return the computed value for the current step.

```python
        traverse(0)
```
- Start the recursive process from step `0` (the bottom of the staircase).

```python
        return dp[0]
```
- Return the number of ways to climb the stairs from the 0th step, stored in `dp[0]`.

---

## 🔁 Summary

- This solution uses **top-down recursion with memoization**.
- It avoids recalculating overlapping subproblems by storing them in a `dp` array.
- The final answer is computed starting from the bottom (step 0) and stored in `dp[0]`.

## 🧠 Note

- The line `ans = 0` is **not used** and can be removed to make the code cleaner.
