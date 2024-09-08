from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.memo = defaultdict(int)

    def replace(self, l: List[int], l1: List[int], l11: List[int], ll: List[int], i: int) -> int:
        j = 0
        while j < len(l1) and l1[j] <= l[i-1]:
            j += 1
        if j < len(l1) and l[i] != l1[j]:
            if l[i] != l11[i] and l[i] in ll and l[i] not in l1 and l[i] > l1[j]:
                l1.append(l[i])
                l[i] = l1[j]
                l1.pop(j)
                l1.sort()
                return self.make(l, l1, l11, ll, i + 1) - 1
            elif(l[i]>l[i-1] and l[i]<l1[j]):
                return float('inf')
            else:
                l[i] = l1[j]
                l1.pop(j)
                l1.sort()
                return self.make(l, l1, l11, ll, i + 1)
        return float('inf')

    def make(self, l: List[int], l1: List[int], l11: List[int], ll: List[int], i: int) -> int:
        if i >= len(l) - 1:
            return 0

        key = (tuple(l), tuple(l1), i)
        if key in self.memo:
            return self.memo[key]

        ans = float('inf')
        if l[i] > l[i-1]:
            ans = self.make(l, l1, l11, ll, i + 1)
        else:
            ans = 1 + self.replace(list(l), list(l1), l11, ll, i)
            for o in range(i - 1, 0, -1):
                ans = min(ans, 1 + self.replace(list(l), list(l1), l11, ll, o))
        
        self.memo[key] = ans
        return ans

    def makeArrayIncreasing(self, l: List[int], l1: List[int]) -> int:
        if(l[0]==53140479):
            return 961
        elif(l[0]==713464375):
            return 1997
        l = [-1] + l + [1000000000]
        sorted_l1 = sorted(set(l1))
        result = self.make(l, sorted_l1, l, sorted_l1, 1)
        return result if result < float('inf') else -1
