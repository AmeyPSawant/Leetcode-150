# P3 - Two Sum

## Links to Practice

Neetcode - https://neetcode.io/problems/two-integer-sum <br/>
Leetcode - https://leetcode.com/problems/two-sum

## Problem Statement

<img src ="P3-PS.png" height="500px"></img>

## Solutions with Time and Space Complexities

### Brute Force

_Checks every possible pair until it finds one that adds up to the target._

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if(i != j and nums[i]+nums[j] == target):
                    return [i,j]
```

**Time**: O(n<sup>2</sup>)<br/>
**Space**: O(1)

<hr/>

### Optimized

_Uses a hash map to find complements in one pass, avoiding nested loops._

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in visited):
                return sorted([i,visited[diff]])
            else:
                visited[nums[i]] = i
```

**Time**: O(n)<br/>
**Space**: O(n)
