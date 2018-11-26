class Player(object):
	def __init__(self, side, board):
		self.side = side
		self.captured_pieces = []
		self.board = board

	def get_captured_pieces():
		return self.captured_pieces

	def make_move(self, piece, origin, destination):
		if is_legal_move(piece, origin, destination):
			self.board.move_piece(piece, origin, destination)

	def is_legal_move(self, piece, origin, destination):
		if origin != piece.get_location():
			return False
		if isInCheck():
			if move in legalMovesCheck():
				return True
			else:
				return False
		else:
			if destination in piece.legal_moves():
				return True
			else:
				return False
				
	def get_captured_pieces():
		return self.captured_pieces

	def is_legal_drop(self, piece, destination):
		if piece not in self.get_captured_pieces():
			return False
		if self.board.has_piece_at(destination[0], destination[1]):
			return False
		if piece is Pawn:
			if not self.is_legal_pawn_drop(piece, destination):
				return False
		return True

	def is_legal_pawn_drop(self, pawn, destination):
		row = destination[1]
		col = destination[0]
		if player.side == 'lower':
			if row == self.board.get_num_rows() - 1:
				return False
		else:
			if row == 0:
				return False
		for movingRow in range(self.board.get_num_rows()):
			if board.piece_at(col, movingRow) is Pawn:
				return False
		if isCheckMate(): #TODO!!!!
			return False
		return True

	def make_drop(self, piece, destination):
		if self.is_legal_drop(piece, destination):
			self.board.drop_piece(piece, destination)
		



