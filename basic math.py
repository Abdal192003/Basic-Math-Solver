# AUTHOR=ABDAL AHMAD KHAN
# PROGRAM NAME = BASIC MATH SOLVER
# DATE=3rd MARCH 2023

# creating particular class for particular function
class circle:
    # self keyword using in function 
    def circle(self):
        r = int(input("Enter the radius"))
        AreaCircle = 3.14*r*r
        print(AreaCircle)

# putting class in object 
c = circle()
# calling the function using object
c.circle()

# created a class 
class square:
    # self keyword is used in this function
    def square(self):
        a = int(input("Enter the area"))
        AreaSquare = a*a
        print(AreaSquare)

# putting the class in object
sq=square()
# calling out the function using object
sq.square()

# created a class
class rectangle:
    # self keyword is used in this function
    def rectangle(self):
       print("Enter the length and Breadth")
       l = int(input("Enter the length"))
       b = int(input("Enter the breadth"))
       AreaRectangle = l*b
       print(AreaRectangle)
       perimeterRectangle = 2*l+2*b
       print("The perimeter of the rectangle is:", perimeterRectangle)

# putting class in object
rec=rectangle()
# calling the function using object
rec.rectangle()

# created a class
class triangle:
    # self keyword used in this function 
    def triangle(self):
       print("Enter the side and perpendicular length for triangle Area")
       s = int(input("Enter the sides of the triangle"))
       p = int(input("Enter the length of perpendicular"))
       AreaTriangle = 1/2*s*p
       print("The Area of Triangle is:", AreaTriangle)

# putting the class in object
tri=triangle()
# calling the function using object 
tri.triangle()

# created a class
class rhombus:
    # self keyword used in this function 
    def rhombus(self):
      print("Enter the Diagonal Length for Rhombus Area ")
      d1 = int(input("Enter the Diagonal length 1"))
      d2 = int(input("Enter the Digonal length 2"))
      AreaDiagonal = 1/2*d1*d2
      print("The Area of Rhombus is :", AreaDiagonal)

# putting the class in object
rho=rhombus()
# calling the function using object
rho.rhombus()

# created a class
class parallelogram:
    # self keyword used in this function
    def parallelogram(self):
        s1 = int(input("Enter the lenght 1"))
        s2 = int(input("Enter the lenght 2"))
        h = int(input("Enter the perpendicular length or Height"))
        AreaParallelogram = 1/2*h*(s1+s2)
        print("The Parallelogram length is:", AreaParallelogram)

# putting the class in object 
par=parallelogram()
# calling the function using object
par.parallelogram()

# created a class 
class sphere:
    # self keyword used in this function 
    def sphere(self):
       print("Now give radius for obtaining sphere area")
       rs = int(input("Enter the radius for sphere"))
       AreaSphere = 4/3*3.14*rs*rs
       print("The Area of the sphere is:", AreaSphere)

# putting the class in object
sh=sphere()
# calling the function using object
sh.sphere()

# created a class 
class cone:
    # self keyword is used in this function 
    def cone(self):
        print("Now give Suitable data for obtaining the cone area")
        sc = int(input("Enter the sides length of the cone"))
        hc = int(input("Enter the Height of the cone"))
        AreaCone = 1/3*hc*sc
        print("The Area of the cone is :", AreaCone)

# putting the class in object
co=cone()
# calling the function using object
co.cone()

