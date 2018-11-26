import Util

class Game(object):
	def __init__(self, mode, file = None):
		self.board = Board()
		self.moves = 0
		self.map = ['a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4]
		self.turn = 'lower'
		self.lower = Player('lower', self.board)
		self.upper = Player('UPPER', self.board)
		self.mode = mode
		self.file = file
		self.piece_map = ['r' : Rook(self.board), 'b' : Bishop(self.board), 's' : SilverGeneral(self.board),\
		'g' : GoldGeneral(self.board), 'k' : King(self.board), 'p' : Pawn(self.board)]

	def run(self):
		print_board() #print without move
		while game_not_end():
			if mode == 'i':
				if in_check(player):
					check_print()
				move = input("> ")
				move = process_move(move)
				print_board() #print move as well




	def process_file(self):
		parsed = Util.parseTestCase(file)
		initial_pieces = parsed['initialPieces']
		upper_captures = parsed['upperCaptures']
		lower_captures = parsed['lowerCaptures']
		moves = parsed['moves']
		for piece in initial_pieces:
			coord = convert_letter_coord_to_num_coord()
			self.board.set_piece_at()


	def game_not_end():

	def print_board():
		print(Util.stringifyBoard(self.board))

	def get_turn():
		return self.turn

	def get_lower():
		return self.lower

	def get_upper():
		return self.upper

	def process_move(move):
		move = move.split()
		if move[0] == 'move':
			origin = move[1]
			destination = move[2]
			origin = (self.map[origin[0]], origin[1]) #bug, need to cast to int
			destination = (self.map[destination[0]], destination[1])
			if get_turn() == 'lower':
				get_lower().make_move(self.board.piece_at(origin[0], origin[1]), origin, destination)
				#TODO handle illegal move game end
			else:
				get_upper().make_move(self.board.piece_at(origin[0], origin[1]), origin, destination)
		elif move[0] == 'drop':
			piece = move[1]
			destination = move[2]
			destination = (self.map[destination[0]], destination[1])

			if get_turn() == 'lower':
				for captured_piece in get_lower().get_captured_pieces():
					if str(captured_piece) == piece:
						piece = captured_piece
				get_lower().make_drop(piece, destination)
			else:
				for captured_piece in get_upper().get_captured_pieces():
					if str(captured_piece) == piece:
						piece = captured_piece
				get_upper().make_drop(piece, destination)
		#TODO else return error 

	def convert_letter_coord_to_num_coord(self, letter_coord):
		return (self.map[letter_coord[0]], int(letter_coord[1]) 

	def convert_letter_piece_to_obj_piece(self, letter_piece):
		return self.piece_map[letter_piece.lower()]    

	def set_piece(self, piece):
		if letter_piece.isLower():
			side = 'lower'
		else:
			side = 'UPPER'
		letter_piece = letter_piece.lower()
		obj_piece = 
		if letter_piece == 'r':
			obj_piece = Rook(side, position[0], position[1], self.board)



	def in_check():

	def check_print():
