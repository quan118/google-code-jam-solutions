from functools import reduce
import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

def round1(num):
  return int(Decimal(num).quantize(Decimal('1')))

def solve(N, L, C, cid):
  need = [0] * (N+1)
  marker = 0
  best_choice = 0
  for i in range(1,N+1):
    tmp = i * 1000 // N
    d = tmp % 10
    if d == 0 or d >= 5:
      if best_choice <= 0 and d >= 5:
        best_choice = i
      need[i] = 0
      if marker > 0:
        for j in range(marker, i):
          need[j] = i - j
        marker = 0
    elif marker <= 0:
      marker = i
  # print(need)

  # print('best_choice:%d' % best_choice)
  unknown = N - reduce(lambda x, y: x + y, C)
  # print('unknown:%d' % unknown)

  C1 = []
  for c in C:
    if best_choice > 0 and need[c] < best_choice:
      C1.append(need[c])

  # for i in range(n_best_choice):
  #   C1.append(best_choice)
  # print(C1)
  C1.sort()
  acc = reduce(lambda x, y: x + y, map(lambda c: round1(c*100/N), C))
  # print('acc:%d' % acc)
  for c in C1:
    unknown -= c
    if unknown < 0:
      unknown += c
      break
    if c > 0:
      acc += 1 + round1(c*100/N)
      # print('acc:%d' % acc)
  # print('acc2:%d' % acc)
  n_best_choice = 0
  if best_choice > 0 and unknown > 0:
    n_best_choice = unknown // best_choice

  for i in range(n_best_choice):
    acc += round1(best_choice*100/N)
    unknown -= best_choice
    if unknown < 0:
      unknown += best_choice
      break
  
  if unknown > 0:
    acc += round1(unknown*100/N)

  print('Case #%d: %d' % (cid+1, acc))

if __name__=="__main__":
  T = int(input())
  for cid in range(T):
    N, L = [int(n) for n in input().split()]
    C = [int(n) for n in input().split()]
    solve(N, L, C, cid)