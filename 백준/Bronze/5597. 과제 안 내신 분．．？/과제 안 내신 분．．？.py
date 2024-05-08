student = []
for i in range (1, 31):
    student.append(i)

for a in range (1, 29):
    student.remove(int(input()))
    
print(min(student))
print(max(student))