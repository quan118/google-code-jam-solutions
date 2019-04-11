
def solve(waffle, R, C, H, V, cid):
  nchip = 0
  for r in range(R):
    for c in range(C):
      if waffle[r][c] == '@':
        nchip += 1
  npieces = (V+1)*(H+1)

  if nchip % npieces != 0 or nchip % H != 0 or nchip % V != 0:
    print('Case #%d: IMPOSSIBLE' % (cid+1))
    return
  
  possible = True
  nchip_in_a_row = nchip // H
  cnt = 0
  r = R
  for r in range(R):
    for c in range(C):
       
    if cnt == nchip_in_a_row:
      cnt = 0
      r -= 1
    elif cnt > nchip_in_a_row:
      possible = False
      break

  pass

if __name__=="__main__":
  T = int(input())
  for cid in range(T):
    R, C, H, V = [int(n) for n in input().split()][:4]
    waffle = []
    for _ in range(R):
      line = input()
      waffle.append(line)
    solve(waffle, R, C, H, V, cid)
