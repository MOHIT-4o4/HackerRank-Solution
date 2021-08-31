# second largest element in nested list
import heapq

students = []
n = int(input())
for i in range(0, n):
    n = [input(), float(input())]
    students.append(n)
    students.sort()
    # students.remove(min(students, key=lambda x: x[1]))
# minim = students.remove(min(students, key=lambda x: x[1]))

minimum = heapq.nsmallest(2, students,key=lambda x:x[0])[-1]
print(minimum,"\n",students)
