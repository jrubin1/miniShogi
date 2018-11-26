import sys

class Main(object):
	def main():
		if sys.argv[1] == '-i':
			game = Game('i')
		elif sys.argv[1] == '-f':
			game = Game('f', sys.argv[2])
		# else:
			#todo throw error incorrect args
		game.run()

	if __name__ == "__main__":
		main()
