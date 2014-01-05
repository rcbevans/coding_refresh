'''
Basically we have a peg-solitaire board:

[1,1,1,1,1,0,1,1,1,1]
1's represent a peg, and 0 is an open spot. You must move a peg one at a time TWO SLOTS backwards or forward ONLY to an empty spot. If you jump over another peg in the process it becomes an empty slot. 
'''

from copy import copy

def tryNextSolution(board):
	print "Current board", board
	board1 = copy(board)
	board2 = copy(board)
	for peg in range(len(board)):
		if board1[peg]:
			if peg > 1 and not board1[peg - 2] and board1[peg-1]:
				board1[peg] = 0
				board1[peg-1] = 0
				board1[peg-2] = 1
				if boardSolved(board1):
					return (True, board1)
				else:
					(success, board1) = tryNextSolution(board1)
					if success:
						return (True, board1)
			if peg < len(board2) - 2 and not board2[peg+2] and board2[peg+1]:
				board2[peg] = 0
				board2[peg+1] = 0
				board2[peg+2] = 1
				if boardSolved(board2):
					return (True, board2)
				else:
					(success, board2) = tryNextSolution(board2)
					if success:
						return (True, board2)

	return (False, board)

def boardSolved(board):
	count = 0
	for peg in board:
		if peg:
			count += 1
	return count == 1


if __name__ == '__main__':
	gameboard = [1,0,1,1,1,1,1,1,1]
	solved, board = tryNextSolution(gameboard)
	print "Solved ", solved, "board", board