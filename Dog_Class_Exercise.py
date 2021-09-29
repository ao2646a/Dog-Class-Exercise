
####EXERCISE
#parent class
class Dogs:
	def __init__(self, name, age, sex, is_barking):
		self.name = name
		self.age = age
		self.sex = sex
		self.is_barking = is_barking
		#method
	def bark_check(self):
		if (self.is_barking == "is barking"):
			print(self.name, "is barking")
		else:
			print(self.name, "is not barking")

#subclass
class Pitbull(Dogs):
	def __init__(self, name, age, sex, is_barking,
		weight, height, head_size, good_gaurd_dog):
		super().__init__(name, age, sex, is_barking)
		self.weight = weight
		self.height = height
		self.head_size = head_size
		self.good_gaurd_dog = good_gaurd_dog

def main ():
	dog_1 = Pitbull(name = "Leo", age = "2", sex = "male", is_barking = "is barking", weight = "60 lb", height = "21 in", head_size = "22 in", good_gaurd_dog = "TRUE")
	dog_1.bark_check()

if __name__ == '__main__':
	main()