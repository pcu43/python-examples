class Dog:
	def __init__(self):
		print("a dog is born")
	def __len__(self):
		return 42
def main():
	d = Dog()
	print(len(d))

if __name__ == "__main__":
	main()
