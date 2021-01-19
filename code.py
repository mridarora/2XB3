def are_valid_groups(Student_Number[], groups[]):
        for i in Student_Number:
            for j in groups:
                if i == j:
                    return True
                else:
                    return False 