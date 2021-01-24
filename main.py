from typing import List
import random


class Solution:

  def __init__(self, w: List[int]):
    self.w = []

    sum = 0

    for num in w:
      sum += num
      self.w.append(sum)

    print(self.w)

  def pickIndex(self) -> int:
    num = random.randint(1, self.w[-1])

    l = 0
    r = len(self.w) - 1
    print('target = ', num)

    # binary search
    while (l < r):
      m = (l+r) // 2

      print('%d, l= %d, r= %d, m= %d' % (self.w[m], l, r, m))

      if num <= self.w[m]:
        r = m
      else:
        l = m + 1

    print('ans = %d' % l)

    return l


# my = Solution([1, 3])
# my = Solution([1])
my = Solution([1, 3, 1])
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
print(my.pickIndex())
'''
[0-0, 1-3]

wSize = 1 + 3 = 4

i = randrange(0,wSize)


[1,3]
1 => 0.75

0 => 0.25

16
[3, 17, 18, 25]

l = 0 , r = 3
m = 2

# binary search

16 < 18 => left => r = mid
l = 0 , r = 2
m = 1
16 < 17 => left => r = mid
l = 0 , r = 1
16 > 3 => right => l = mid
l = 1, r = 1

return 1
'''
