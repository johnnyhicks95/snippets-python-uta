# ejemplo 1 , ingresar y nombrar nombres alfabeticamente
names= []
for i in range(5):
    n=input("Enter a name")
    names.append(n)
print("Entered names are ",names)
names.sort()
print("Sortered names are ",names)


# sample 2 encontrar el promedio de notas de estudiante
names = []
marks = []
for i in range(5):
    n=input("Enter student name: ")
    m =int(input("Enter marks of student "))
    names.append(n)
    marks.append(m)
h=max(marks)
l=min(marks)
print("Highest marks are ",h)
print("Lowest marks are: ", l)

for i in range(5):
    if h==marks[i]:
        print("Student having highest mark is ", names[i])
    if l==marks[i]:
        print("Student hacing lowest mark is ", names[i])

# write a program to input a value and insert it in the middle of an existing list
A=[12,34,56,11,24,65,76]
print("List is ", A)
num=int(input("Enter number to be inserted in the list "))
pos=int(("enter the position to insert the number "))
A.insert(pos,num)
print("Modified list", A)