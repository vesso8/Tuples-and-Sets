number_of_students = int(input())
students_data = {}
def avg_result(average):
    return sum(average) / len(average)

for _ in range(number_of_students):
    name , grade = tuple(input().split())
    if not name in students_data:
        students_data[name] = []
    students_data[name].append(float(grade))

for key, value in students_data.items():
    average_grade = avg_result(value)
    grades_data = ' '.join(map(lambda grade: f'{grade:.2f}', value))
    print(f"{key} -> {grades_data} (avg: {average_grade:.2f})")