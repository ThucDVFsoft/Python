#Viết chương trình nhập vào một ngày trong thế kỉ 21 và cho biết ngày đó là thứ mấy trong tuần
import datetime

weekday = { 0: "Monday",
			1: "Tuesday",
			2: "Wednesday",
			3: "Thursday",
			4: "Friday",
			5: "Saturday",
			6: "Sunday"}
def weekday_of_date(year, month, day):
	date = datetime.date(year, month, day)
	day  = date.weekday()
	return weekday[day]

print(weekday_of_date(2020,1,17))
