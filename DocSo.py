#Viết chương trình chuyển một số trong phạm vi 0-999 thành dạng văn bản theo phát âm tiếng Việt, ví dụ 102 → 'một trăm lẻ hai'

def read_number(num):
	if num > 999 or num < 0:
		return
	
	num_dic = {'0': 'không',
			   '1': 'một',
			   '2': 'hai',
			   '3': 'ba',
			   '4': 'bốn',
			   '5': 'năm',
			   '6': 'sáu',
			   '7': 'bảy',
			   '8': 'tám',
			   '9': 'chín'}
	
	template = ["mot", "trăm", "hai", "mươi", "tư"]
	string = str(num).zfill(3)
	
	template[0] = num_dic[string[0]]
	template[2] = num_dic[string[1]]
	template[4] = num_dic[string[2]]
	
	out = ' '.join(template)

	if "không trăm" in out:
		out = out.replace("không trăm ", "")
		if "không mươi" in out:
			out = out.replace("không mươi", "")

	if "không mươi" in out:
		out = out.replace("không mươi", "lẻ ")
		out = out.replace("  ", " ")
	if "một mươi" in out:
		out = out.replace("một mươi", "mười")
		out = out.replace("  ", " ")
	if "lẻ không" in out:
		out = out.replace("lẻ không", "")
		out = out.replace("  ", " ")
	if "mươi một" in out:
		out = out.replace("mươi một", "mươi mốt")
		out = out.replace("  ", " ")
	return out.strip()
	
	
print(read_number(151))
		
		
	
	