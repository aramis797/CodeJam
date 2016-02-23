from sys import stdin
T = int(stdin.readline())
for t in range(T):
	print 'Case #%d: %s' % (t+1,' '.join(reversed(stdin.readline().split())))
