import pandas as pd

def main(get_student):
    return get_student

students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"}, 
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"}, 
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell Terrier"}, 
    {"name":"Draco", "house":"Slytherin", "patronus":"Snake"}, 
    {"name":"Neville", "house":"Gryffindor", "patronus":"Tawny Owl"}, 
    {"name":"Snape", "house":"Slytherin", "patronus":"Greyhound"}, 
    {"name":"Luna", "house":"Ravenclaw", "patronus":"Hare"}, 
    {"name":"Ginny", "house":"Gryffindor", "patronus":"Horse"} 
    ]

df = pd.DataFrame(students)

print(df)

for student in students:
    print(f"{student['name']} is in {student['house']} and their patronus is a {student['patronus']}.")


# def get_student(index):
#     for student in students:
#         if students.index(student) == index:
#             return student
        
# which_stud = int(input("Enter student number (1-8): "))
# print(main(get_student(which_stud - 1)))
# print(ranking := "Ranking of students:")
# for i in range(len(students)):
#     print(f"{i+1}: {students[i]}")