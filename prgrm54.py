
class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        sec = self.__second + other.__second
        minute = self.__minute + other.__minute
        hour = self.__hour + other.__hour

        minute += sec // 60
        sec = sec % 60

        hour += minute // 60
        minute = minute % 60

        return Time(hour, minute, sec)

    def display(self):
        print("Sum of time:", self.__hour, "hours",
              self.__minute, "minutes",
              self.__second, "seconds")


# Getting user input
h1 = int(input("Enter hours of first time: "))
m1 = int(input("Enter minutes of first time: "))
s1 = int(input("Enter seconds of first time: "))

h2 = int(input("Enter hours of second time: "))
m2 = int(input("Enter minutes of second time: "))
s2 = int(input("Enter seconds of second time: "))

# Creating objects
t1 = Time(h1, m1, s1)
t2 = Time(h2, m2, s2)

# Adding two time objects
t3 = t1 + t2

# Displaying result
t3.display()

