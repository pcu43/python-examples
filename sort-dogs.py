class Dog:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
	def __str__(self):
		return "{{ \"name\": \"{}\", \"weight\": {} }}".format(self.name, self.weight)
	def __repr__(self):
		return "{{ \"name\": \"{}\", \"weight\": {} }}".format(self.name, self.weight)
def getweight(d):
	return d.weight
def main():
	d = Dog('sparky',15)
	d1 = Dog('zeus',10)
	d2 = Dog('spike',23)
	dogs = [d, d1, d2]
	print(dogs)
	dogs.sort
	print(dogs)
	dogs.sort(key=getweight)
	print(dogs)

if __name__ == "__main__":
	main()
