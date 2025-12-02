

d={'name':'alice','marks':98.5}

m1=input("enter name of student:")
if m1 in d['name']:
        print(f"marks of {m1}:{d['marks']}")
else:
        print("student name not found")

