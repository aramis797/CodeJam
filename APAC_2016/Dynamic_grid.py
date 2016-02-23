from sys import stdin
def getOnesCount(grid):
	count=0
	for row in grid:
		for val in row:
			if val == 1:
				count+=1
	return count
def Operation_M(grid,row,col,val):
	grid[row][col]=val;
def Operation_Q(grid):
	onesCount=getOnesCount(grid)
	out=0
for _t in range(int(stdin.next())):
	R,C = [int(x) for x in stdin.next().split()]
	grid=[]
	for row in range(R):
		grid.append([int(x) for x in stdin.next().strip()])
count=0
print getOnesCount(grid)