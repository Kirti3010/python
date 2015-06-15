class Avenger:    #class
	avengersCount = 0      #class variable

	def __init__(self,name,power):             #whatever in the class variable 
		Avenger.avengersCount += 1      #are called instance methods
		self.name = name              #init is d constructor
		self.power = power

	def howMany():
		print("Total Avengers %d" % Avenger.avengersCount)

	def getName(self):
		print("Avengers Name: "+self.name+"have Power"+self.power)

   #creating new objects of class variable(update)
hulk=Avenger("hulk","Angryness")
print(hulk.name)
print(hulk.power)

print("avengersCount: ", Avenger.avengersCount)
Avenger.howMany()

print("########################\n")
ironman=Avenger("ironman","stealness")

print(ironman.name)
print(ironman.power)

print("avengersCount: ", Avenger.avengersCount)
Avenger.howMany()

print("#######################")

blackwidow=Avenger("blackwidow","current")
print(blackwidow.name)
print(blackwidow.power)

print("avengersCount: ", Avenger.avengersCount)
Avenger.howMany()

print("########################\n")

hulk.size="very big"                #creating the attributes of a object
print("hulk size is",hulk.size)

del hulk.power                    #deleting the attribute of a object
print(hulk.name)

print(getattr(hulk,'name'))
print(setattr(hulk,"name","badahulk"))
print(hulk.name)