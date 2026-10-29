def simple_interest(p,t,senior):
 if senior=="yes":
  r=12
 else:
  r=10
 return(p*t*r)/100
p=float(input("enter principal amount:"))
t=float(input("enter time in years:"))
senior=input("are you a senior citizen?(yes/no):").lower()
si=simple_interest(p,t,senior)
print("simple interest=",si)
 
