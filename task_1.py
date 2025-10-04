student_name = input('enter student name: ')
a = {
"Alice": 85,
"Bob": 92,
"Charlie": 78,
"Diana": 95,
"Eve": 88,
"Frank": 73,
"Grace": 90
}
if student_name in a:
    print (f"{student_name}'s marks :- {a[student_name]}")
else :
    print('student name not found')
