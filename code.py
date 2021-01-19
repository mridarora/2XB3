def are_valid_groups(student_numbers,groups):
	dict = {}
	lis = []
	
	for i in student_numbers:
		dict[i] = 0

	for i in student_numbers:
		for j in groups:
			if i in j:
				dict[i] += 1	

	for i in groups:
		if len(i) == 2 or len(i) == 3:
			lis.append(True)

	ans = all(lis)

	for i in dict:
		if dict[i] < 1 or ans == False
			return False

	return True
		
