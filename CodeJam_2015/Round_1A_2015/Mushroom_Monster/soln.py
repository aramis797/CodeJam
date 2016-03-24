def first_method(M, N):
  min_eat = 0
  for i in range(1, N):
    min_eat += max(0, M[i - 1] - M[i])
  return min_eat

def second_method(M, N):
  max_rate = 0
  for i in range(1, N):
    max_rate = max(max_rate, M[i - 1] - M[i])

  min_eat = 0
  # exclude the last mushroom
  for i in range(0, N - 1):
    min_eat += min(M[i], max_rate)
  return min_eat

for tc in range(int(input())):
  N = int(input())
  M = map(int, raw_input().split())
  print "Case #%d: %d %d" % (tc + 1,
    first_method(M, N), second_method(M, N))