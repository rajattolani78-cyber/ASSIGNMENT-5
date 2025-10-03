t = input('enter student name: ')
a = {
"Alice": 85,
"Bob": 92,
"Charlie": 78,
"Diana": 95,
"Eve": 88,
"Frank": 73,
"Grace": 90
}
if t in a:
    print (f"{t}'s marks :- {a[t]}")
else :
    print('student name not found')
