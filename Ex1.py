import numpy as np
import sys
row = [2, 1, -1, -2, -2, -1, 1, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1]



# Validarea coodonatelor calului pentru a nu iesi din tabla de sah
def isValid(x, y, N, board):
    return not (x < 0 or y < 0 or x >= N or y >= N or board[x][y]!=0)


# functia recursiva pentru algoritmul calului folosing backtracking
def knightTour(x, y, pos, N, board):
	

	if pos == N * N + 1:
		print(board)
		print('Solutia a fost gasita!!')
		sys.exit()
		return

	# verificarea tuturor posibilelor mutari ale calului
	for move in range(8):
		# modificare pozitiei calului pe tabla de sah
		newX = x + row[move]
		newY = y + col[move]
		# verificarea daca noua pozitie e valida si nevizitata
		if isValid(newX, newY, N, board):
			board[newX][newY] = pos
			knightTour(newX, newY, pos + 1, N, board)

	board[x][y] = 0


if __name__ == '__main__':
	# `N × N` chessboard
	N = int(input("Dim tabla: "))
	a = int(input("X= "))
	b = int(input("Y= "))


	board = np.zeros((N, N))
	pos = 2
	board[a][b] = 1
	knightTour(a, b, pos, N, board)
