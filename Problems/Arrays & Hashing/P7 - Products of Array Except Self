# P7 - Products of Array Except Self

## Links to Practice

Neetcode - https://neetcode.io/problems/products-of-array-discluding-self <br/>
Leetcode - https://leetcode.com/problems/product-of-array-except-self/

## Problem Statement

<img src ="P7-PS.png" height="500px"></img>

## Solutions with Time and Space Complexities

### Brute Force

_For each element, multiplies every other element in the list except itself._

```
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        i = 0
        prods = []
        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if i != j:
                    p *= nums[j]
            prods.append(p)
        return prods
```

**Time**: O(n<sup>2</sup>)<br/>
**Space**: O(n)

<hr/>

### Optimized

_Calculates prefix and suffix products in two passes to get the product of all elements except the current one._

```
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1]*len(nums)

        p = 1
        for i in range(len(nums)):
            result[i] = p
            p *= nums[i]

        s = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= s
            s *= nums[i]

        return(result)
```

**Time**: O(n)<br/>
**Space**: O(1)
