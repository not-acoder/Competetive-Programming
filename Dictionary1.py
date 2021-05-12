
n = int(input())
student_marks = {}
x=0
marks = []
hello = []
j=0


for i in range(n):
    name = input("Enter name")
    for j in range(3):
        print("Enter marks")
        y=input()
        hello.append(y)
    marks.append(hello)
    hello =[]  # set temp_list to null
    student_marks[name]= marks
    marks=[]

key = input()

if student_marks.get(key)!=None:
    a = int(student_marks[key][0][0])
    b = int(student_marks[key][0][1])
    c = int(student_marks[key][0][2])
    print(a,b,c)
    d=a+b+c
    e=d/3.0
    e=round(e,2)
    print(e)