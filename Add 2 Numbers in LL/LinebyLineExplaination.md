# Line-by-Line Explanation of `addTwoNumbers`

```python
# Definition for singly-linked list.
```
**Explanation**: Definition for singly-linked list.

```python
# class ListNode:
```
**Explanation**: class ListNode:

```python
#     def __init__(self, val=0, next=None):
```
**Explanation**: def __init__(self, val=0, next=None):

```python
#         self.val = val
```
**Explanation**: self.val = val

```python
#         self.next = next
```
**Explanation**: self.next = next

```python
class Solution:
```

```python
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
```

```python
        carry = 0  # To store carry from sum of two digits
```
**Explanation**: To store carry from sum of two digits

```python
        head = ListNode()  # Dummy head node to simplify list construction
```
**Explanation**: Dummy head node to simplify list construction

```python
        temp = head  # Pointer to build the result list
```
**Explanation**: Pointer to build the result list

```python
        while l1 or l2:
```

```python
            v1 = l1.val if l1 else 0  # Get value from l1 or 0 if l1 is exhausted
```
**Explanation**: Get value from l1 or 0 if l1 is exhausted

```python
            v2 = l2.val if l2 else 0  # Get value from l2 or 0 if l2 is exhausted
```
**Explanation**: Get value from l2 or 0 if l2 is exhausted

```python
            s = v1 + v2 + carry  # Sum of both digits and carry
```
**Explanation**: Sum of both digits and carry

```python
            carry = s // 10  # Update carry for next iteration
```
**Explanation**: Update carry for next iteration

```python
            s = s % 10  # Get the single digit to store in current node
```
**Explanation**: Get the single digit to store in current node

```python
            temp.val = s  # Set current node value
```
**Explanation**: Set current node value

```python
            l1 = l1.next if l1 else None  # Move to next node in l1 if available
```
**Explanation**: Move to next node in l1 if available

```python
            l2 = l2.next if l2 else None  # Move to next node in l2 if available
```
**Explanation**: Move to next node in l2 if available

```python
            if l1 or l2:
```

```python
                temp.next = ListNode()  # Create next node in result list
```
**Explanation**: Create next node in result list

```python
                temp = temp.next  # Move temp to next node
```
**Explanation**: Move temp to next node

```python
            else:
```

```python
                if carry:
```

```python
                    temp.next = ListNode(val=carry)  # Add carry as a new node if exists
```
**Explanation**: Add carry as a new node if exists

```python
                else:
```

```python
                    temp.next = None  # No further nodes
```
**Explanation**: No further nodes

```python
        return head  # Return the dummy head which points to the result
```
**Explanation**: Return the dummy head which points to the result

