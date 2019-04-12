def solve(N, L, C, cid):
  C1 = []
  for c in C:
    tmp = c * 1000 // N
    last_digit = tmp % 10
    if last_digit >= 5:
      continue
    else:
      C1.append((5-last_digit)*N//10)
  C1.sort()
  tmp = 1000 // N
  last_digit = tmp % 10
  best_choice = 1
  if last_digit < 5:
    best_choice += (5-last_digit)*N//10
  

if __name__=="__main__":
  T = int(input())
  for cid in range(T):
    N, L = [int(n) for n in input().split()]
    C = [int(n) for n in input().split()]
    solve(N, L, C, cid)