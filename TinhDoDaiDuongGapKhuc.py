import math


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	

def length(p1, p2):
	return math.sqrt(pow((p1.x-p2.x), 2) + pow((p1.y-p2.y), 2))


def polyline_length(points):
	ret = 0
	for ind in range(len(points)-1):
		ret += length(points[ind], points[ind+1])

	return ret


p1 = Point(5, 0)
p2 = Point(10, 5)
p3 = Point(6, 5)
ps = [p1, p2, p3]
print(polyline_length(ps))
