
#s = True
#v = False
#print(s & v)
#print(5^6)
#print(~7)

#Task 1

#A = True
#B = False
#F = A & B or A & ~B
#print("Task 1:", F)

#Task 2
A = bool(input("A:"))
B = bool(input("B:"))
I= bool(input("C:"))
F = (A or B) & (not B or I) & ( not(I)) 
print("Task 2:", F)
#A B C F
#0 0 0 0
#0 0 1 0
#0 1 0 0
#0 1 1 0
#1 0 0 
#1 0 1
#1 1 0
#1 1 1 