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
					
							
