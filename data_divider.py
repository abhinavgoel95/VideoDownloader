data = []
curfileno = 0
with open('streamlink_list.txt', 'r') as f:
	for ind, line in enumerate(f.readlines()):
		fileno = ind//50
		if fileno == curfileno:
			data.append(line)
		else:
			with open('streamlink_list'+str(curfileno)+'.txt', 'w') as f1:
				for listitem in data:
					f1.write(listitem)
			data = []
		curfileno = fileno
	with open('streamlink_list'+str(curfileno)+'.txt', 'a') as f1:
		for listitem in data:
			f1.write(listitem)	
