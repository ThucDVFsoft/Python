class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
#Shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
def polygon_area(points):
	area = 0
	noSide = len(points)
	for i in range(noSide - 1):
		area += (points[i].x * points[i+1].y) - (points[i+1].x * points[i].y)
		
	area += (points[noSide - 1].x * points[0].y) - (points[0].x * points[noSide - 1].y)
	area = 0.5 * abs(area)
	
	return area
	

ps = [Point(0, 0), Point(0, 8), Point(8, 0), Point(8, 9), Point(5, 1)]

print(polygon_area(ps))