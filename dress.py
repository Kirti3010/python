class Dress():
	dresscount = 0

	def __init__(self,color,size):
		Dress.dresscount += 1
		self.color = color
		self.size = size

	def howMuch():
		print("Total selled Dress=%d" %Dress.dresscount)

	def specification():
		print("Color" +self.color+ "size" +self.size+)
