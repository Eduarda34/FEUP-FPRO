def top_avg(grades):
    top_student = None
    highest_avg = 0

    for student, grades_list in grades.items():
        avg = sum(grades_list) / len(grades_list)

        if avg > highest_avg or (avg == highest_avg and student < top_student):
            top_student = student
            highest_avg = avg

    return top_student

print(top_avg({ 2024003:[14,16], 2024002:[11,13], 2024001:[15] }))
print(top_avg({ 2024003:[14,15,13,10], 2024002:[18,15,13], 2024001:[14,14] }))
print(top_avg({ 2024003:[10], 2024002:[10,10,10], 2024001:[20,10,13] }))
print(top_avg({ 2024003:[10,10,10,10] }))