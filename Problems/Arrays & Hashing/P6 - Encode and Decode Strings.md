# P6 - Encode and Decode Strings

## Links to Practice

Neetcode - https://neetcode.io/problems/string-encode-and-decode <br/>
Leetcode - https://leetcode.com/problems/encode-and-decode-strings

## Problem Statement

<img src ="P6-PS.png" height="500px"></img>

## Solutions with Time and Space Complexities

### Brute Force

_Builds one long string where each word is stored as length + “#” + word, and then parses it back out by reading length first._

```
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res
```

**Time**: O(n)<br/>
**Space**: O(n)
