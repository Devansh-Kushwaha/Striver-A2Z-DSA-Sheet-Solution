# 🧠 Intuition

Each position in the digit string has fixed valid choices:
- At **even indices** (0-based), only **even digits** (0, 2, 4, 6, 8) are allowed → **5 choices**.
- At **odd indices**, only **prime digits** (2, 3, 5, 7) are allowed → **4 choices**.

The number of ways to form a good number of length `n` is:
- \( 5^{\text{even positions}} \times 4^{\text{odd positions}} \)

The number of even positions is:
- \( \lceil \frac{n}{2} \rceil \)

The number of odd positions is:
- \( \lfloor \frac{n}{2} \rfloor \)

Since the values can be very large, we use **modular exponentiation** with modulo \( 10^9 + 7 \) to compute powers efficiently.

---

# 🛠️ How to Solve

1. **Count even and odd indices:**
   - If `n` is odd: even positions = \( \frac{n}{2} + 1 \), odd = \( \frac{n}{2} \)
   - If `n` is even: even = odd = \( \frac{n}{2} \)

2. **Create a modular exponentiation function (`power`):**
   - Use binary exponentiation to compute large powers modulo \( 10^9 + 7 \)

3. **Compute result as:**
   - \( \text{result} = (5^\text{even} \mod MOD) \times (4^\text{odd} \mod MOD) \mod MOD \)

4. **Return the result.**

This approach is efficient even for very large `n` (up to \( 10^{15} \)) due to the logarithmic time complexity of the power function.

