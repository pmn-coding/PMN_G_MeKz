from random import randint

signs = ['Rock', 'Paper', 'Scissors']

rw = 1
pw = 1
sw = 1
rl = 1
pl = 1
sl =1
rr = 0.0
pr = 0.0
sr = 0.0
rc = 0
pc = 0
sc = 0


win = 0
winc = 0

while not win == 200 or  winc == 200:
	
	ys = input('Your Sign(Rock, Paper, Scissors): ')
	
	if rr > sr and rr > pr:
		if not rc == 3:
			cs = signs[0]
			rc += 1
		else:
			rc = 0
			cs = signs[randint(0,2)]
			
	elif pr > rr and pr > sr:
		if not pc == 3:
			cs = signs[1]
			pc += 1
		else:
			pc = 0
			cs = signs[randint(0,2)]
			
	elif sr > rr and sr > pr:
		if not sc == 3:
			cs = signs[2]
			sc += 1
		else:
			sc = 0
			cs = signs[randint(0,2)]
	else:
		cs = signs[randint(0,2)]	
		
	if ys in signs:
		if ys == cs:
			print('Tie. Next round.')
		else:
			if ys == 'Rock':
				if cs == 'Paper':
					winc += 1
					pw += 1
					print('You lost. Next round.')
				else:
					win += 1
					sl += 1
					print('You won. Next round.')
			elif ys == 'Paper':
				if cs == 'Scissors':
					winc += 1
					sw += 1
					print('You lost. Next round.')
				else:
					win += 1
					rl += 1
					print('You won. Next round.')
			else:
				if cs == 'Rock':
					winc += 1
					rw += 1
					print('You lost. Next round.')
				else:
					win += 1
					pl += 1
					print('You won. Next round.')
	else:
		print('Invalid sign')
	
	rr = rw/rl
	pr = pw/pl
	sr = sw/sl
	
if win == 7:
	print('You won.')
	print('I won', winc, 'times.')
else:
	print('I won.')
	print('You won', win,'times.')