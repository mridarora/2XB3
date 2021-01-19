def are_valid_groups(student_numbers,groups):
	dict = {}
	
	for i in student_numbers:
		dict[i] = 0

	for i in student_numbers:
		for j in groups:
			if i in j:
				dict[i] += 1	

	for i in dict:
		if dict[i] == 1
			return False
	return True
		
