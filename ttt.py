import random
 

Board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

'''
Board displayed as:
	1 2 3
	4 5 6
	7 8 9
'''

def displayBoard():
	for x in range(0, 9):
		print Board[x],
		if x == 2:
			print '\n'
		if x == 5:
			print '\n'
	print '\n'

def checkWin():
	# check horizontal win for x
	if Board[0] == 'x' and Board[1] == 'x' and Board[2] == 'x':
		print('Player one wins!')
		raise SystemExit 
	elif Board[3] == 'x' and Board[4] == 'x' and Board[5] == 'x':
		print('Player one wins!')
		raise SystemExit
	elif Board[6] == 'x' and Board[7] == 'x' and Board[8] == 'x':
		print('Player one wins!')
		raise SystemExit
	# check vertical win for x
	elif Board[0] == 'x' and Board[3] == 'x' and Board[6] == 'x':
		print('Player one wins!')
		raise SystemExit
	elif Board[1] == 'x' and Board[4] == 'x' and Board[7] == 'x':
		print('Player one wins!')
		raise SystemExit
	elif Board[2] == 'x' and Board[5] == 'x' and Board[8] == 'x':
		print('Player one wins!')
		raise SystemExit
	# check diagonal win for x
	elif Board[0] == 'x' and Board[4] == 'x' and Board[8] == 'x':
		print('Player one wins!')
		raise SystemExit
	elif Board[2] == 'x' and Board[4] == 'x' and Board[6] == 'x':
		print('Player one wins!')
		raise SystemExit
	
	# check horizontal win for o
	elif Board[0] == 'o' and Board[1] == 'o' and Board[2] == 'o':
		print('Player two wins!')
		raise SystemExit
	elif Board[3] == 'o' and Board[4] == 'o' and Board[5] == 'o':
		print('Player two wins!')
		raise SystemExit
	elif Board[6] == 'o' and Board[7] == 'o' and Board[8] == 'o':
		print('Player two wins!')
		raise SystemExit
	# check vertical win for o
	elif Board[0] == 'o' and Board[3] == 'o' and Board[6] == 'o':
		print('Player two wins!')
		raise SystemExit
	elif Board[1] == 'o' and Board[4] == 'o' and Board[7] == 'o':
		print('Player two wins!')
		raise SystemExit
	elif Board[2] == 'o' and Board[5] == 'o' and Board[8] == 'o':
		print('Player two wins!')
		raise SystemExit
	# check diagonal win for o
	elif Board[0] == 'o' and Board[4] == 'o' and Board[8] == 'o':
		print('Player two wins!')
		raise SystemExit
	elif Board[2] == 'o' and Board[4] == 'o' and Board[6] == 'o':
		print('Player two wins!')
		raise SystemExit

	# check draw
	elif (Board[0] == 'x' or Board[0] == 'o') and (Board[1] == 'x' or Board[1] == 'o') and (Board[2] == 'x' or Board[2] == 'o') and (Board[3] == 'x' or Board[3] == 'o') and (Board[4] == 'x' or Board[4] == 'o') and (Board[5] == 'x' or Board[5] == 'o') and (Board[6] == 'x' or Board[6] == 'o') and (Board[7] == 'x' or Board[7] == 'o') and (Board[8] == 'x' or Board[8] == 'o'):
		print('Draw!')
		raise SystemExit

def twoPlayer():
	print('Player one is X, Player two is O. Choose a number to select a spot.')

 	displayBoard()

	for x in range (0, 20):
		choice1 = input('Player one\'s turn: ')
		if choice1 == 1:
			if Board[0] == 'x' or Board[0] == 'o':
				print('Not an Option.')
			else:
				Board[0] = 'x'
		elif choice1 == 2:
			if Board[1] == 'x' or Board[1] == 'o':
				print('Not an Option.')
			else:
				Board[1] = 'x'
		elif choice1 == 3:
			if Board[2] == 'x' or Board[2] == 'o':
				print('Not an Option.')
			else:
				Board[2] = 'x'
		elif choice1 == 4:
			if Board[3] == 'x' or Board[3] == 'o':
				print('Not an Option.')
			else:
				Board[3] = 'x'
		elif choice1 == 5:
			if Board[4] == 'x' or Board[4] == 'o':
				print('Not an Option.')
			else:
				Board[4] = 'x'
		elif choice1 == 6:
			if Board[5] == 'x' or Board[5] == 'o':
				print('Not an Option.')
			else:
				Board[5] = 'x'
		elif choice1 == 7:
			if Board[6] == 'x' or Board[6] == 'o':
				print('Not an Option.')
			else:
				Board[6] = 'x'
		elif choice1 == 8:
			if Board[7] == 'x' or Board[7] == 'o':
				print('Not an Option.')
			else:
				Board[7] = 'x'
		elif choice1 == 9:
			if Board[8] == 'x' or Board[8] == 'o':
				print('Not an Option.')
			else:
				Board[8] = 'x'
		else:
			print('Not an Option.')

		displayBoard()
		checkWin()

		choice2 = input('Player two\'s turn: ')
		if choice2 == 1:
			if Board[0] == 'x' or Board[0] == 'o':
				print('Not an Option.')
			else:
				Board[0] = 'o'
		elif choice2 == 2:
			if Board[1] == 'x' or Board[1] == 'o':
				print('Not an Option.')
			else:
				Board[1] = 'o'
		elif choice2 == 3:
			if Board[2] == 'x' or Board[2] == 'o':
				print('Not an Option.')
			else:
				Board[2] = 'o'
		elif choice2 == 4:
			if Board[3] == 'x' or Board[3] == 'o':
				print('Not an Option.')
			else:
				Board[3] = 'o'
		elif choice2 == 5:
			if Board[4] == 'x' or Board[4] == 'o':
				print('Not an Option.')
			else:
				Board[4] = 'o'
		elif choice2 == 6:
			if Board[5] == 'x' or Board[5] == 'o':
				print('Not an Option.')
			else:
				Board[5] = 'o'
		elif choice2 == 7:
			if Board[6] == 'x' or Board[6] == 'o':
				print('Not an Option.')
			else:
				Board[6] = 'o'
		elif choice2 == 8:
			if Board[7] == 'x' or Board[7] == 'o':
				print('Not an Option.')
			else:
				Board[7] = 'o'
		elif choice2 == 9:
			if Board[8] == 'x' or Board[8] == 'o':
				print('Not an Option.')
			else:
				Board[8] = 'o'
		else:
			print('Not an Option.')

		displayBoard()
		checkWin()




def onePlayer():
	print('Player one is X, Computer is O. Choose a number to select a spot.')

	displayBoard()

	for x in range (0, 20):
		choice1 = input('Player one\'s turn: ')
		if choice1 == 1:
			if Board[0] == 'x' or Board[0] == 'o':
				print('Not an Option.')
			else:
				Board[0] = 'x'
		elif choice1 == 2:
			if Board[1] == 'x' or Board[1] == 'o':
				print('Not an Option.')
			else:
				Board[1] = 'x'
		elif choice1 == 3:
			if Board[2] == 'x' or Board[2] == 'o':
				print('Not an Option.')
			else:
				Board[2] = 'x'
		elif choice1 == 4:
			if Board[3] == 'x' or Board[3] == 'o':
				print('Not an Option.')
			else:
				Board[3] = 'x'
		elif choice1 == 5:
			if Board[4] == 'x' or Board[4] == 'o':
				print('Not an Option.')
			else:
				Board[4] = 'x'
		elif choice1 == 6:
			if Board[5] == 'x' or Board[5] == 'o':
				print('Not an Option.')
			else:
				Board[5] = 'x'
		elif choice1 == 7:
			if Board[6] == 'x' or Board[6] == 'o':
				print('Not an Option.')
			else:
				Board[6] = 'x'
		elif choice1 == 8:
			if Board[7] == 'x' or Board[7] == 'o':
				print('Not an Option.')
			else:
				Board[7] = 'x'
		elif choice1 == 9:
			if Board[8] == 'x' or Board[8] == 'o':
				print('Not an Option.')
			else:
				Board[8] = 'x'
		else:
			print('Not an Option.')

		displayBoard()
		checkWin()

		
		print('Computer\'s turn: ')

		'''
		0 1 2
		3 4 5
		6 7 8
		'''
		if Board[4] == '5':
			Board[4] = 'o'
			displayBoard()
			continue

		# horizontal block
		# first row
		if Board[0] == 'x' and Board[1] == 'x' and Board[2] != 'o':
			Board[2] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[0] == 'x' and Board[2] == 'x' and Board[1] != 'o':
			Board[1] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[1] == 'x' and Board[2] == 'x' and Board[0] != 'o':
			Board[0] = 'o'
			displayBoard()
			checkWin()
			continue
		# second row
		if Board[3] == 'x' and Board[4] == 'x' and Board[5] != 'o':
			Board[5] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[3] == 'x' and Board[5] == 'x' and Board[4] != 'o':
			Board[4] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[4] == 'x' and Board[5] == 'x' and Board[3] != 'o':
			Board[3] = 'o'
			displayBoard()
			checkWin()
			continue
		# third row
		if Board[6] == 'x' and Board[7] == 'x' and Board[8] != 'o':
			Board[8] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[6] == 'x' and Board[8] == 'x' and Board[7] != 'o':
			Board[7] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[7] == 'x' and Board[8] == 'x' and Board[6] != 'o':
			Board[6] = 'o'
			displayBoard()
			checkWin()
			continue

		# vertical block
		# first column
		if Board[0] == 'x' and Board[3] == 'x' and Board[6] != 'o':
			Board[6] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[0] == 'x' and Board[6] == 'x' and Board[3] != 'o':
			Board[3] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[3] == 'x' and Board[6] == 'x' and Board[0] != 'o':
			Board[0] = 'o'
			displayBoard()
			checkWin()
			continue
		# second column
		if Board[1] == 'x' and Board[4] == 'x' and Board[7] != 'o':
			Board[7] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[1] == 'x' and Board[7] == 'x' and Board[4] != 'o':
			Board[4] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[4] == 'x' and Board[7] == 'x' and Board[1] != 'o':
			Board[1] = 'o'
			displayBoard()
			checkWin()
			continue
		# third column
		if Board[2] == 'x' and Board[5] == 'x' and Board[8] != 'o':
			Board[8] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[2] == 'x' and Board[8] == 'x' and Board[5] != 'o':
			Board[5] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[5] == 'x' and Board[8] == 'x' and Board[2] != 'o':
			Board[2] = 'o'
			displayBoard()
			checkWin()
			continue

		# diagonal block
		if Board[0] == 'x' and Board[4] == 'x' and Board[8] != 'o':
			Board[8] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[4] == 'x' and Board[8] == 'x' and Board[0] != 'o':
			Board[0] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[2] == 'x' and Board[4] == 'x' and Board[6] != 'o':
			Board[6] = 'o'
			displayBoard()
			checkWin()
			continue
		if Board[4] == 'x' and Board[6] == 'x' and Board[2] != 'o':
			Board[2] = 'o'
			displayBoard()
			checkWin()
			continue



		
		def chooseSpot():
			choice2 = random.randint(1, 9)
			if choice2 == 1:
				if Board[0] == 'x' or Board[0] == 'o':
					chooseSpot()
				else:
					Board[0] = 'o'
			if choice2 == 2:
				if Board[1] == 'x' or Board[1] == 'o':
					chooseSpot()
				else:
					Board[1] = 'o'
			if choice2 == 3:
				if Board[2] == 'x' or Board[2] == 'o':
					chooseSpot()
				else:
					Board[2] = 'o'
			if choice2 == 4:
				if Board[3] == 'x' or Board[3] == 'o':
					chooseSpot()
				else:
					Board[3] = 'o'
			if choice2 == 5:
				if Board[4] == 'x' or Board[4] == 'o':
					chooseSpot()
				else:
					Board[4] = 'o'
			if choice2 == 6:
				if Board[5] == 'x' or Board[5] == 'o':
					chooseSpot()
				else:
					Board[5] = 'o'
			if choice2 == 7:
				if Board[6] == 'x' or Board[6] == 'o':
					chooseSpot()
				else:
					Board[6] = 'o'
			if choice2 == 8:
				if Board[7] == 'x' or Board[7] == 'o':
					chooseSpot()
				else:
					Board[7] = 'o'
			if choice2 == 9:
				if Board[8] == 'x' or Board[8] == 'o':
					chooseSpot()
				else:
					Board[8] = 'o'
		
		chooseSpot()

		displayBoard()
		checkWin()




x = input('Press 1 for one player, press 2 for two player:   ')

if x == 2:
	twoPlayer()
elif x == 1:
	onePlayer()
else: 
	print ('Not a valid option.')




	
