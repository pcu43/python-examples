with open('dog.txt') as f:
	lines = f.readlines()
for line in lines:
	print(line.strip())
