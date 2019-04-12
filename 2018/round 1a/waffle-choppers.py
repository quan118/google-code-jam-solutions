def solve(waffle, R, C, H, V, cid):
  nchip = 0
  for r in range(R):
    for c in range(C):
      if waffle[r][c] == '@':
        nchip += 1
  npieces = (V+1)*(H+1)

  if nchip % npieces != 0 or nchip % (H+1) != 0 or nchip % (V+1) != 0:
    print('Case #%d: IMPOSSIBLE' % (cid+1))
    return
  
  possible = True
  nchip_in_a_row = nchip // (H + 1)
  cnt = 0
  rows = []
  cols = []
  for r in range(R):
    for c in range(C):
       if waffle[r][c] == '@':
         cnt += 1
    if cnt == nchip_in_a_row:
      cnt = 0
      rows.append(r)
    elif cnt > nchip_in_a_row:
      possible = False
      break
  
  if possible:
    nchip_in_a_col = nchip // (V+1)
    for c in range(C):
      for r in range(R):
        if waffle[r][c] == '@':
          cnt += 1
      if cnt == nchip_in_a_col:
        cnt = 0
        cols.append(c)
      elif cnt > nchip_in_a_col:
        possible = False
        break
  
  r0 = 0
  c0 = 0
  cnt = 0
  nchip_per_piece = nchip // npieces

  for r1 in rows:
    for c1 in cols:
      cnt = 0
      for r in range(r0, r1+1):
        for c in range(c0, c1+1):
          if waffle[r][c] == '@':
            cnt += 1
      c0 = c1 + 1
      if cnt != nchip_per_piece:
        possible = False
        break
    if possible == False:
      break
    r0 = r1 + 1
    c0 = 0

  if possible:
    print('Case #%d: POSSIBLE' % (cid+1))
  else:
    print('Case #%d: IMPOSSIBLE' % (cid+1))

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
