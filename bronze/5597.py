student_check_book = list()
dont_homework_students = list()

for _ in range(28):
    a = int(input())
    student_check_book.append(a)

for sd in range(1,31):
    if sd not in student_check_book:
        dont_homework_students.append(sd)

print(" ".join(map(str,dont_homework_students)))
