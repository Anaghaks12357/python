
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    # Overloading > operator
    def __gt__(self, other):
        return self.area() > other.area()


# Getting user input
l1 = float(input("Enter length of Rectangle 1: "))
w1 = float(input("Enter width of Rectangle 1: "))

l2 = float(input("Enter length of Rectangle 2: "))
w2 = float(input("Enter width of Rectangle 2: "))

# Creating objects
r1 = Rectangle(l1, w1)
r2 = Rectangle(l2, w2)

# Displaying areas
print("Area of Rectangle 1:", r1.area())
print("Area of Rectangle 2:", r2.area())

# Comparing areas
if r1 > r2:
    print("Rectangle 1 has greater area")
elif r2 > r1:
    print("Rectangle 2 has greater area")
else:
    print("Both rectangles have equal area")

