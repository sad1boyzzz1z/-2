f = open('Perepis.txt', 'r')
while True:
	line = f.readln()
	a = len(line)
	if (line[a-2] <=7) and (line[a-1]<8):
		b = line.split()
		print(b[0],b[1],b[2])

diapazon1 = input()
diapazon2 = input()
while True:
	lines = f.readln()
	b = len(lines)
	if (str(lines[b-2]+lines[b-1]) == diapazon1) or (str(lines[b-2]+lines[b-1]) == diapazon2):
		g = lines.split()
		print(b[0], b[1], b[2])