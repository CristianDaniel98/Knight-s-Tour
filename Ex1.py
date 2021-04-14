import numpy as np
import sys
row = [2, 1, -1, -2, -2, -1, 1, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1]

'''
Pe aici nu trimiteai N
'''
# Check if `(x, y)` is valid chessboard coordinates.
# Note that a knight cannot go out of the chessboard
def isValid(x, y, N, board):
    return not (x < 0 or y < 0 or x >= N or y >= N or board[x][y]!=0)


'''
Nici aici nu trimiteai N
'''
# Recursive function to perform the knight's tour using backtracking
def knightTour(x, y, pos, N, board):
	#print(board)

	# if all squares are visited, print the solution

	'''
		Ai pornit cu matricea full 0, deci 0 e nevizitat
		atunci 1 va fi prima pozitie de pe care pleci
		si n*n+1 e ultima posibila
	'''
	if pos == N * N + 1:
		print(board)
		print('Solutia a fost gasita!!')
		sys.exit()
		return

	# check for all eight possible movements for a knight
	# and recur for each valid movement
	for move in range(8):
		# get the new position of the knight from the current
		# position on the chessboard
		newX = x + row[move]
		newY = y + col[move]
		# if the new position is valid and not visited yet
		if isValid(newX, newY, N, board):
			board[newX][newY] = pos
			knightTour(newX, newY, pos + 1, N, board)

	# backtrack from the current square and remove it from the current path
	board[x][y] = 0


if __name__ == '__main__':
	# `N × N` chessboard
	N = int(input("Dim tabla: "))
	a = int(input("X= "))
	b = int(input("Y= "))

	'''
	Cum aveai inainte board = visited = np.zeros,
	practic, board era referinta la visited, daca o modificai
	pe una, se modifica si cealalta.

	Oricum, nu vad de ce ai folosi doua matrici identice.
	'''
	board = np.zeros((N, N))
	pos = 2
	board[a][b] = 1

	# start knight tour from corner square `(0, 0)`
	knightTour(a, b, pos, N, board)