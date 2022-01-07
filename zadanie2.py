f = open('Perepis.txt')
while True:
	linejdd = f.readline()
	a = len(linejdd)
	if (linejdd[a-2] <=7) and (linejdd[a-1]<8):
		b = linejdd.split()
		print(b[0],b[1],b[2])

diapazon1 = input()
diapazon2 = input()
while True:
	liness = f.readline()
	b = len(liness)
	if (str(liness[b-2]+liness[b-1]) == diapazon1) or (str(liness[b-2]+liness[b-1]) == diapazon2):
		g = liness.split()
		print(b[0], b[1], b[2])