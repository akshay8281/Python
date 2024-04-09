print("Student Result Details")

sname = input("Enter a Name : ")
rno = int(input("Enter a Roll No. : "))
s1 = int(input("Enter Subject 1 : "))
s2 = int(input("Enter Subject 2 : "))
s3 = int(input("Enter Subject 3 : "))

total = s1+s2+s3

per = total/3

print("Student name : ",sname)
print("Student Roll no. : ",rno)
print("Student Total : ",total)
print("Student Percentage : ",per)


if per>=70:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass Class")
else:
    print("Fail")
