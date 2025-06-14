# 📘 Line-by-Line Explanation: Subsets using DFS (Backtracking)

```python
class Solution:
```
- Defines a class `Solution` that contains our subset-generating method.

```python
    def subsets(self, nums: List[int]) -> List[List[int]]:
```
- Defines the method `subsets` which takes a list of integers and returns a list of all possible subsets (power set).

```python
        temp = []
```
- Initializes an empty list `temp` to store all non-empty subsets.

```python
        n = len(nums)
```
- Stores the length of the input list `nums` for reuse in recursion.

```python
        def traverse(l, i):
```
- Declares a helper function `traverse` used for recursive traversal.
- `l` is the current subset being formed.
- `i` is the current index in the input list.

```python
            nonlocal temp
```
- Allows the inner function to modify the outer variable `temp`.

```python
            if l and i == n:
                temp.append(l)
```
- If we reach the end of the list (`i == n`) and the current subset `l` is not empty, append `l` to `temp`.

```python
            if i >= n:
                return
```
- If the index `i` exceeds or reaches the length of the list, terminate this branch of recursion.

```python
            traverse(l + [nums[i]], i + 1)
```
- Recursive call including the current element `nums[i]` in the subset.

```python
            traverse(l, i + 1)
```
- Recursive call excluding the current element `nums[i]` from the subset.

```python
            return
```
- End of current recursion branch.

```python
        traverse([], 0)
```
- Start the recursion with an empty subset and index 0.

```python
        return [[]] + temp
```
- Add the empty subset manually and return the final list of all subsets.

---

# 🔍 Summary

- We use recursive backtracking to explore all inclusion/exclusion combinations.
- Each element has two choices: include or exclude.
- All valid subsets are collected in `temp`.
- The empty subset is added separately.

---

# 🧪 Example

Input:
```python
nums = [1, 2]
```

Output:
```python
[[], [1], [2], [1, 2]]
```
