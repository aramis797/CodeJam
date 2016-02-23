from sys import stdin
from UserString import MutableString
BLANK='.'
RED='R'
BLUE='B'

#Gravity to right (shift all R's and B's to right)
def gravityToRight(grid,n):
	newGrid=[]
	for i in xrange(n):
		newGrid.append(MutableString('.'*n))
	for y in range(n):
		shiftedx=n-1
		for x in range(n-1,-1,-1):
			if(grid[y][x] != BLANK):
				newGrid[y][shiftedx]=grid[y][x]
				shiftedx-=1
	return newGrid

#count max consicutive number for a piece
def countPiecesInRow(grid,piece,x,y,dx,dy,n):
	maximum=0
	counter=0
	while(x>=0 and y>=0 and x<n and y<n):
		if(grid[x][y] == piece):
			counter+=1
			maximum = max(maximum,counter)
		else:
			counter=0
		x+=dx
		y+=dy
	return maximum

#find winning pieces
def isWinning(grid,n,k,piece):
	for i in range(n):
		#grid[x][y]
		#y will change for each x,Horizontal
		if(countPiecesInRow(grid,piece,i,0,0,1,n) >= k):
			return True
		#x will change for each y, Vertical
		if(countPiecesInRow(grid,piece,0,i,1,0,n) >= k):
			return True
		#Upper TOP RIGHT -> BOTTOM LEFT
		if(countPiecesInRow(grid,piece,0,i,1,-1,n) >= k):
			return True
		#
		if(countPiecesInRow(grid,piece,i,n-1,1,-1,n) >= k):
			return True
		if(countPiecesInRow(grid, piece, i, 0, 1, 1, n) >= k):
			return True
		if(countPiecesInRow(grid, piece, 0, i, 1, 1, n) >= k):
			return True
	return False

T = int(stdin.next())
for i in range(1,T+1):
	n,k = tuple([int(x) for x in stdin.next().split()])
	grid=[]
	for j in range(n):
		grid.append(MutableString(stdin.next().strip()))
	

	grid=gravityToRight(grid,n)

	redHasWon = isWinning(grid,n,k,RED)
	blueHasWon = isWinning(grid,n,k,BLUE)

	if(redHasWon and blueHasWon):
		result="Both"
	elif(redHasWon):
		result = "RED"
	elif(blueHasWon):
		result="BLUE"
	else:
		result="Neither"
	print "Case #%d %s "%(i,result)