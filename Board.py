import Util

class Board(object):
	def __init__(self):
		self.board = initialize_default()
		self.num_rows = len(self.board[0])
		self.num_cols = len(self.board[0][0])

	def make_board(self, rows, cols):
		return [['' for x in range(cols)] for i in range(rows)]

	def initialize_default(self):
		#change this to set to pieces
		board = make_board(5, 5)
		board[0][0] = 'k'
		board[1][0] = 'g'
		board[2][0] = 's'
		board[3][0] = 'b'
		board[4][0] = 'r'
		board[0][1] = 'p'

		board[0][4] = 'R'
		board[1][4] = 'B'
		board[2][4] = 'S'
		board[3][4] = 'G'
		board[4][4] = 'K'
		board[4][3] = 'P'

		return board

	def set_piece_at(self, coord, piece):
		board[coord[0]][coord[1]] = piece

	def has_piece_at(self, col, row):
		if self.board[col][row] != '':
			return True
		else:
			return False

	def piece_at(self, col, row):
		return self.board[col][row]

	def get_num_rows():
		return self.num_rows

	def get_num_cols():
		return self.num_cols

	def drop_piece(self, piece, destination):
		col = destination[0]
		row = destination[1]
		self.board[col][row] = piece
		piece.set_location(destination)


	def move_piece(self, piece, origin, destination):
		orig_col = origin[0]
		orig_row = origin[1]
		dest_col = destination[0]
		dest_row = destination[1]
		self.board[dest_col][dest_row] = self.board[orig_col][orig_row]
		self.board[orig_col][orig_row] = None
		piece.set_location(destination)



if __name__ == "__main__":
	board = Board()
	print(board.board)
	print('a')
	board.board[0][0] = 'a'
	board.board[4][4] = 'z'
	board.board[0][1] = 'b'
	board.board[1][0] = 'x'
	print(Util.stringifyBoard(board.board))





