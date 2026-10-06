names=input("enter first name seperated by space:").split()
count=0
for name in names:
 count += name.lower().count('a')
 name.lower().count('a')
print("no of occurrence of 'a':",count)
