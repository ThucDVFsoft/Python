#Để định vị một điểm trên mặt đất, người ta dùng tọa độ GPS gồm kinh độ, vĩ độ, (và độ cao). Trên
#bản đồ Hà Nội, hồ Hoàn Kiếm có vĩ độ là 21.0259198, kinh độ 105.8444646 . Lăng Bác có vĩ độ
#21.0379367, kinh độ 105.8324912. Biết bán kính trái đất là 6371 km, bạn hãy tính khoảng cách theo
#đường chim bay từ hồ Hoàn Kiếm đến lăng Bác.

#Formular 
#Haversine
#formula:	a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
#c = 2 ⋅ atan2( √a, √(1−a) )
#d = R ⋅ c
#where	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
#note that angles need to be in radians to pass to trig functions!
import math


class Point:
	def __init__(self, x, y):
		self.lat = x
		self.lon = y
		
		
R = 6371000
def Distance(p1, p2):
	phi1 = toRadians(p1.lat)
	phi2 = toRadians(p2.lat)
	del_phi = toRadians(p2.lat - p1.lat)
	del_lamda = toRadians(p2.lon - p1.lon)
	
	a = pow(math.sin(del_phi/2), 2) + math.cos(phi1) * math.cos(phi2) * pow(math.sin(del_lamda/2),2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = R * c
	return d


def toRadians(degree):
	return degree * (math.pi/180)
	
p1 = Point(105.8444646, 21.0259198)
p2 = Point(105.8324912, 21.0379367)

print(Distance(p1, p2))