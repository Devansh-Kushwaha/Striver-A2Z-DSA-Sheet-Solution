# Intuition

The two numbers are represented in **reverse order** using linked lists, where each node contains a single digit.  
The goal is to add the numbers digit-by-digit, just like how we would add two numbers by hand, starting from the least significant digit (units place), while keeping track of the **carry**.

---

# Approach

1. Initialize a dummy `head` node to start building the resulting linked list.
2. Use a `temp` pointer to construct the new list and a `carry` variable to handle digits overflow.
3. Traverse both `l1` and `l2` simultaneously:
   - For each node, extract the values (`v1` and `v2`), defaulting to 0 if a list is exhausted.
   - Compute the sum of `v1 + v2 + carry`.
   - Update `carry = sum // 10` and store `sum % 10` as the new node value.
4. If either `l1` or `l2` still has nodes, create a new node and move the `temp` pointer forward.
5. After the loop, if there’s a remaining `carry`, add a new node with that value.
6. Return the `head` node of the result list.

---

# Complexity

- **Time complexity**:  
  $$O(\max(n, m))$$  
  Where `n` and `m` are the lengths of the two linked lists.

- **Space complexity**:  
  $$O(\max(n, m))$$  
  A new linked list is created to store the result, proportional to the length of the longer input list.
