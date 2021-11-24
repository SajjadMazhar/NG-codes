import math
class Circle:
	pi=4*(math.atan(1))
	def get_area(self, radius):
		return self.pi*radius*radius
	
	def get_circum(self, radius):
		return 2*self.pi*radius

circle=Circle()
circle.radius=10
area=circle.get_area(circle.radius)
circumference=circle.get_circum(circle.radius)
print('circumference of the circle is: ',circumference)
print('area of the circle is: ',area)
