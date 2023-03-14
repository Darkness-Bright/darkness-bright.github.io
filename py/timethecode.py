def test():
  global bigsum
  bigsum = sum(range(100))

import timeit
times = 1000

howmanyseconds_test = timeit.timeit("test()",number=times,setup="from __main__ import test")/times

print(bigsum,howmanyseconds_test)