print("WELCOME TO THE TRIANGLE PERIMETER PROGRAM")
print('Enter the coordinates of the vertices of a triangle...')

#Vertex A
print('\nVertex A')
xA = int(input('Enter x-coordinate for Vertex A: '))
yA = int(input('Enter y-coordinate for Vertex A: '))

#Vertex B 
print('\nVertex B')
xB = int(input('Enter x-coordinate for Vertex B: '))
yB = int(input('Enter y-coordinate for Vertex B: '))

#Vertex C
print('\nVertex C')
xC = int(input('Enter x-coordinate for Vertex C: '))
yC = int(input('Enter y-coordinate for Vertex C: '))

#dist function
def dist(x1, y1, x2, y2):
    return (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

#Find perimeter and side lenths
AB = dist(xA, yA, xB, yB)
AC = dist(xA, yA, xC, yC)
BC = dist(xB, yB, xC, yC)
perimeter = AB + AC + BC

#Print Values
print("\nSIDE LENGTHS & PERIMETER")
print('AB = ' + str(AB))
print('AC = ' + str(AC))
print('BC = ' + str(BC))
print('Perimeter = ' + str(perimeter))