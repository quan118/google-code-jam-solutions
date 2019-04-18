from functools import reduce

def round1(num):
  d = int(num * 10) % 10 
  return int(num) if d < 5 else int(num + 1)

def solve(N, L, C, cid):
  need = [0] * (N+1)
  marker = 0
  best_choice = 0
  for i in range(1,N+1):
    tmp = i * 1000 // N
    d = tmp % 10
    if d >= 5:
      best_choice = i if best_choice <= 0 and d >= 5 else best_choice
      need[i] = 0
      if marker > 0:
        for j in range(marker, i):
          need[j] = i - j
        marker = 0
    elif marker <= 0:
      marker = i

  unknown = N - reduce(lambda x, y: x + y, C)


  C1 = [(need[c],c) for c in C]
  C1.sort(key=lambda c1: c1[0])

  acc = 0
  for c1 in C1:
    if c1[0] > best_choice or unknown < c1[0] or c1[0] <= 0:
      acc += round1(c1[1]*100/N)
    else:
      unknown -= c1[0]
      acc += round1((c1[0]+c1[1])*100/N)

  n_best_choice = 0
  if best_choice > 0 and unknown > 0:
    n_best_choice = unknown // best_choice
  acc += n_best_choice * round1(best_choice*100/N)
  unknown -= n_best_choice * best_choice

  if unknown > 0:
    acc += round1(unknown*100/N)

  print('Case #%d: %d' % (cid+1, acc))

if __name__=="__main__":
  T = int(input())
  for cid in range(T):
    N, L = [int(n) for n in input().split()]
    C = [int(n) for n in input().split()]
    solve(N, L, C, cid)