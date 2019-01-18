#Viết chương trình chuyển một xâu chứa phát âm tiếng Việt của một số trong phạm vi 0-999 thành
#giá trị của số đó, ví dụ 'ba trăm hai mươi tư' → 324. Nếu xâu văn bản đầu vào không tương ứng với số
#nào thì thông báo không tồn tại số

def read_char_to_number(string):
	string = string.replace("  ", " ")
	if string.strip() == "một trăm":
		return 100
	num_dic = {'không': '0',
				'lẻ': '0',
			   'một': '1',
			   'mốt': '1',
			   'hai': '2',
			   'ba': '3',
			   'bốn': '4',
			   'tư': '4',
			   'năm': '5',
			   'sáu': '6',
			   'bảy': '7',
			   'tám': '8',
			   'chín': '9'}
	
	string = string.replace("trăm", "")
	string = string.replace("mươi", "")
	strs = string.split()
	
	out = []
	for s in strs:
		out.append(num_dic[s])
	
	return int(''.join(out))
	
	
print(read_char_to_number("chín mươi ba"))