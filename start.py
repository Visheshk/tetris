import numpy
array = numpy.zeros(210).reshape((21, 10))
#array [0][5] = 1
#print array

piecepos = [0,0]
for i in range(0,10):
	array[20][i] = 1

def newpiece():
	array[0][5] = 1
	piecepos[0] = 0
	piecepos[1] = 5

def checkpiece():
	j = 0
	if (array[piecepos[0] + 1][piecepos[1]] == 1):
		j = j + 1
	else:
		print(piecepos)
	return j

def movepiece(dir):
	if dir == 1:
		array[piecepos[0]][piecepos[1]] = 0
		piecepos[0] = piecepos[0] + 1
		array[piecepos[0]][piecepos[1]] = 1
	if dir == 2:
		if array[piecepos[0]][piecepos[1] + 1] == 0:
			array[piecepos[0]][piecepos[1]] = 0
			piecepos[0] = piecepos[0] + 1
			array[piecepos[0]][piecepos[1]] = 1

def checkboard():
	summ = sum(array[0])
	if summ > 0:
		return 1
	else:
		return 0

def piecetravel():
	loop=1
	dir = 1
	while (loop):
		print array
		if (checkpiece()):
			loop=0
		movepiece(dir)
		if (checkpiece()):
			loop=0
		dir = input()

def main():
	loop = 1
	while(loop):
		newpiece()
		piecetravel()
		if(checkboard()):
			loop = 0
main()
#updateboard()

	
	
	
