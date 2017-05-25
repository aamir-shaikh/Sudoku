import argparse
from Tkinter import Tk, Canvas,Frame , Button, BOTH, TOP, BOTTOM

#Globally defined variables
BOARDS = ['debug','bot','shake','error']	#Board Type 
MARGIN = 20 
SIDE = 50 
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9 		# Board Size

class SudokuError(Exception):
	"""
	Defined Errors
	"""
	pass

class GameBoard(object):
	"""
	This class represents the 9X9 board
	"""
	def __init__(self, board_file):
		self.board = self.__create_board(board_file)
		
	def __create_board(self. board_file):
		board = []			#Create an empty list
		
		for line in board_file:
			line =line.strip()
			
			if len(line) != 9:   	#Check if every line is of length 9
				board = []
				raise SudokuError("Sudoku input should contain 9 chars on each line!")
				
				board.append([])
				
				for c in line:
					if not c.isdigit():	#Every item should be an integer
						raise SudokuError("Only digits are considered for Sudoku Input!")
					board[-1].append(int(c))
					
			if len(board) ! = 9:	#The board must have 9 lines to play
				raise SudokuError("Sudoku must contain 9 lines!")
				
			return board
					
							
class Game(object):
	"""
	This checks the state of the board and whther the game is complete
	"""
	def __init__(self, board_file):
		self.board_file = board_file
		self.start_puzzle = GameBoard(board_file).board
	
	def start(self):
		self.game_over = False
		self.puzzle = []
		for i in  xrange(9):
			self.puzzle.append([])
			for j in xrange(9):
				self.puzzle[i].append(self.start_puzzle[i][j])
				
	def check_for_win(self)
		for row in xrange(9):
			if not self.__check_row(row):
				return False
		for column in xrange (9):
			if not self.__check_column(column):
				return False	
		for row in xrange(3):
			for column in xrange(3):
				if not self.__check_square(row,column):
					return False
		self.game_over = True
		return True

def __check_block(self, block):
	return set(block) == set(range(1,10))

def __check_row(self, row):
	return self.__check_block(self.puzzle[row]
	
def __check_column(self, column):
	return self.__check_block([self.puzzle[row][column] for row in xrange(9)])
	
def __check_square(self, block):
	return self.__check_block(
		[
			self.puzzle[r][c]
			for r in xrange(row*3, (row+1) * 3)
			for c in xrange(column *3, (column +1 *3)
		]
	)	
	
	