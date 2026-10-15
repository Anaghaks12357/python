color_list1=input("enter colors for list 1:").split(",")
color_list2=input("enter colors for list 2:").split(",")
print("colors not present in list 2:")
for color in color_list1:
 if color not in color_list2:
   print(color)
