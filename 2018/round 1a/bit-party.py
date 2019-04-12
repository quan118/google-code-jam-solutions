from functools import reduce

def max_time(cashiers):
  mx = 0
  for c in cashiers:
    mx = max(mx, c[0]*c[1]+c[2])
  return mx

def calculate_capacity(cashier, t):
  return max(0, min(cashier[0], (t - cashier[2]) // cashier[1]))

def calculate_capacities(cashiers, t):
  capacities = []
  for c in  cashiers:
    capacities.append(calculate_capacity(c, t))
  capacities.sort(reverse=True)
  return capacities

def solve(R, B, C, cashiers, cid):
  maxT = max_time(cashiers)
  minT = 0
  t = (minT + maxT) // 2
  while minT <= maxT:
    capacities = calculate_capacities(cashiers, t)
    if reduce(lambda x, y: x+y, capacities[:R]) >= B:
      capacities = calculate_capacities(cashiers, t-1)
      if reduce(lambda x, y: x+y, capacities[:R]) < B:
        print('Case #%d: %d' % (cid+1, t))
        break
      else:
        maxT = t-1
    else:
      minT = t+1
    t = (minT + maxT) // 2

if __name__=="__main__":
  T = int(input())
  for cid in range(T):
    R, B, C = [int(n) for n in input().split()]
    cashiers = []
    for _ in range(C):
      M, S, I = [int(n) for n in input().split()]
      cashiers.append((M, S, I))
    solve(R, B, C, cashiers, cid)

