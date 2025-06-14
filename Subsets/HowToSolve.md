# Intuition

The task is to generate all possible subsets (also known as the power set) of a given list of distinct integers.

Each element in the input list has two choices:  
1. **Include** the element in the current subset.
2. **Exclude** the element from the current subset.

This naturally leads to a **binary tree-like recursion**, where we explore both inclusion and exclusion paths at each index. The total number of subsets for a list of size `n` is `2^n`.

---

# How to Solve

1. Use **backtracking (recursive DFS)** to explore all subset combinations.
2. Create a helper function `traverse(l, i)`:
   - `l`: current subset being formed.
   - `i`: current index in the input list.
3. If the current subset `l` is not empty and we've reached the end of the list (`i == n`), we **append it to the result list**.
4. If the index goes out of bounds (`i >= n`), we simply return.
5. We perform two recursive calls:
   - One where `nums[i]` is included in the subset.
   - One where it's not.
6. After recursion, we return the result list including the empty set `[]`, which is the subset of no elements.

---

# Code

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        n = len(nums)

        def traverse(l, i):
            nonlocal temp
            if l and i == n:
                temp.append(l)
            if i >= n:
                return
            
            traverse(l + [nums[i]], i + 1)  # Include nums[i]
            traverse(l, i + 1)             # Exclude nums[i]

            return
        
        traverse([], 0)

        return [[]] + temp  # Add the empty subset manually
