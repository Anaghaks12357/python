n=int(input("enter no of elements:"))
lst=[]
for i in range(n):
     num=int(input("enter a number:"))
     lst.append(num)
total=0
for i in lst:
     total=total+i
print("lst=",lst)
print("sum=",total)
