# 🔢 Count Good Numbers (Optimized with Fast Exponentiation)

## ✅ Problem Summary

We need to count the number of **good digit strings** of length `n`.

A **digit string is good** if:
- Digits at **even indices (0-based)** are **even digits** (0, 2, 4, 6, 8) → 5 choices.
- Digits at **odd indices** are **prime digits** (2, 3, 5, 7) → 4 choices.

---

## 💡 Intuition

Each digit contributes independently to the total count:
- Even-indexed positions have 5 options.
- Odd-indexed positions have 4 options.

So, total number of good digit strings is:
```
(5 ^ #even_positions) * (4 ^ #odd_positions)
```

We use **modular exponentiation** to compute powers efficiently under modulo \( 10^9 + 7 \).

---

## 🧠 Line-by-Line Explanation

```python
class Solution:
```
- Define a class `Solution` that wraps our method.

```python
    def countGoodNumbers(self, n: int) -> int:
```
- Main function that takes input `n` and returns the count of good digit strings.

```python
        e = n // 2
        o = e
        if n % 2 == 1:
            e += 1
```
- Calculate the number of even-indexed (`e`) and odd-indexed (`o`) positions.
- If `n` is odd, even indices get one extra digit.

```python
        ans = 1
        MOD = 10**9 + 7
```
- Initialize answer and the modulo constant.

```python
        def power(num, e):
```
- Define a helper function for **modular exponentiation**.

```python
            ans = 1
            while e > 0:
                if e % 2 == 1:
                    ans *= num
                    ans %= MOD
                    e -= 1
                else:
                    num *= num      
                    num %= MOD
                    e /= 2     
            return ans
```
- Efficiently computes `num^e % MOD` using binary exponentiation.
- If `e` is odd: multiply the result by `num`.
- If `e` is even: square the base and halve the exponent.

> ⚠️ Note: Replace `e /= 2` with `e //= 2` for integer division to avoid float precision issues.

```python
        ans = power(5, e)
```
- Compute \( 5^e \mod MOD \)

```python
        ans *= power(4, o)
```
- Multiply with \( 4^o \mod MOD \)

```python
        ans %= MOD
```
- Apply final modulo to the result.

```python
        return ans
```
- Return the total number of good digit strings modulo \( 10^9 + 7 \)

---

## 🧮 Complexity

- **Time Complexity:**  
  \( O(\log n) \) due to binary exponentiation.

- **Space Complexity:**  
  \( O(1) \), constant space used.

---

## 🧪 Example

Input:
```python
n = 4
```

Even positions = 2 → `5^2 = 25`  
Odd positions = 2 → `4^2 = 16`  
Total = `25 * 16 = 400`

Output:
```
400
```

---

## ✅ Final Tip

Fix integer division:
```python
e //= 2  # instead of e /= 2
```

---

