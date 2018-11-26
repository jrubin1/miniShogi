class Piece:
	def __init__(self, board, side = 'lower', col = 0, row = 0):
		self.row = row
		self.col = col
		self.board = board
		self.side = side

	def get_location(self):
		return (self.col, self.row)

	def set_location(self, location):
		self.col = location[0]
		self.row = location[1]

class King(Piece):
	def legal_moves():
		row_upper_bound = min(self.board.num_rows, self.row + 1)
		row_lower_bound = max(0, self.row - 1)

		col_upper_bound = min(self.board.num_cols, self.col + 1)
		col_lower_bound = max(0, self.col - 1)

		legal_moves = []
		for row in range(row_lower_bound, row_upper_bound + 1):
			for col in range(col_lower_bound, col_upper_bound + 1):
				if self.board.has_piece_at(col, row) and self.board.piece_at(col, row).side == self.side:
					continue
				if row == self.row and col == self.col:
					continue
				else:
					legal_moves.append((col, row))
		return legal_moves

class Rook(Piece):
	def legal_moves():
		legal_moves = []

		north = self.row + 1
		while north < self.board.num_rows:
			if self.board.has_piece_at(self.col, north):
				if self.board.piece_at(self.col, north).side != self.side:
					legal_moves.append(self.col, north)
				break
			else:
				legal_moves.append(self.col, north)
				north += 1

		south = self.row - 1
		while south > -1:
			if self.board.has_piece_at(self.col, south):
				if self.board.piece_at(self.col, south).side != self.side:
					legal_moves.append(self.col, south)
				break
			else:
				legal_moves.append(self.col, south)
				south -= 1

		east = self.col + 1
		while east < self.board.num_cols:
			if self.board.has_piece_at(east, self.row):
				if self.board.piece_at(east, self.row).side != self.side:
					legal_moves.append(east, self.row)
				break
			else:
				legal_moves.append(east, self.row)
				east += 1

		west = self.col - 1
		while west > -1:
			if self.board.has_piece_at(west, self.row):
				if self.board.piece_at(west, self.row).side != self.side:
					legal_moves.append(west, self.row)
				break
			else:
				legal_moves.append(west, self.row)
				west -= 1

		return legal_moves

class Bishop(Piece):
	def legal_moves():
		legal_moves = []

		north_east_col = self.col + 1
		north_east_row = self.row + 1
		while north_east_col < self.board.num_cols and north_east_row < self.board.num_rows:
			if self.board.has_piece_at(north_east_col, north_east_row):
				if self.board.piece_at(north_east_col, north_east_row).side != self.side:
					legal_moves.append(north_east_col, north_east_row)
				break
			else:
				legal_moves.append(north_east_col, north_east_row)
				north_east_col += 1
				north_east_row += 1

		south_west_col = self.col - 1
		south_west_row = self.row - 1
		while south_west_col > -1 and south_west_row > -1:
			if self.board.has_piece_at(south_west_col, south_west_row):
				if self.board.piece_at(south_west_col, south_west_row).side != self.side:
					legal_moves.append(south_west_col, south_west_row)
				break
			else:
				legal_moves.append(south_west_col, south_west_row)
				south_west_col -= 1
				south_west_row -= 1

		south_east_col = self.col + 1
		south_east_row = self.row - 1
		while south_east_col < self.board.num_cols and south_east_row > -1:
			if self.board.has_piece_at(south_east_col, south_east_row):
				if self.board.piece_at(south_east_col, south_east_row).side != self.side:
					legal_moves.append(south_east_col, south_east_row)
				break
			else:
				legal_moves.append(south_east_col, south_east_row)
				south_east_col += 1
				south_east_row -= 1

		north_west_col = self.col - 1
		north_west_row = self.row + 1
		while north_west_col > -1 and north_west_row < self.board.num_rows:
			if self.board.has_piece_at(north_west_col, north_west_row):
				if self.board.piece_at(north_west_col, north_west_row).side != self.side:
					legal_moves.append(north_west_col, north_west_row)
				break
			else:
				legal_moves.append(north_west_col, north_west_row)
				north_west_col -= 1
				north_west_row += 1

		return legal_moves

class GoldGeneral(Piece):
	def legal_moves():
		row_upper_bound = min(self.board.num_rows, self.row + 1)
		row_lower_bound = max(0, self.row - 1)

		col_upper_bound = min(self.board.num_cols, self.col + 1)
		col_lower_bound = max(0, self.col - 1)

		null_squares = [(self.col, self.row)]
		if self.side == 'lower':
			null_squares += [(self.col - 1, self.row - 1), (self.col + 1, self.row - 1)]
		else:
			null_squares += [(self.col - 1, self.row + 1), (self.col + 1, self.row + 1)]

		legal_moves = []
		for row in range(row_lower_bound, row_upper_bound + 1):
			for col in range(col_lower_bound, col_upper_bound + 1):
				if (col, row) in null_squares:
					continue
				if self.board.has_piece_at(col, row) and self.board.piece_at(col, row).side == self.side:
					continue 
				else:
					legal_moves.append((col, row))
		return legal_moves

class SilverGeneral(Piece):
	def legal_moves():
		row_upper_bound = min(self.board.num_rows, self.row + 1)
		row_lower_bound = max(0, self.row - 1)

		col_upper_bound = min(self.board.num_cols, self.col + 1)
		col_lower_bound = max(0, self.col - 1)

		null_squares = [(self.col, self.row)]
		if self.side == 'lower':
			null_squares += [(self.col - 1, self.row), (self.col + 1, self.row), (self.col, self.row - 1)]
		else:
			null_squares += [(self.col - 1, self.row), (self.col + 1, self.row), (self.col, self.row + 1)]

		legal_moves = []
		for row in range(row_lower_bound, row_upper_bound + 1):
			for col in range(col_lower_bound, col_upper_bound + 1):
				if (col, row) in null_squares:
					continue
				if self.board.has_piece_at(col, row) and self.board.piece_at(col, row).side == self.side:
					continue 
				else:
					legal_moves.append((col, row))
		return legal_moves

class Pawn(Piece):
	def legal_moves():
		legal_moves = []
		if self.board.has_piece_at(self.col, self.row + 1):
			if self.board.piece_at(self.col, self.row + 1).side != self.side:
				legal_moves.append(self.col, self.row + 1)
		return legal_moves







		

