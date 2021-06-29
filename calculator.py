a=lambda x,y:x+y
b=lambda x,y:x-y
c=lambda x,y:x*y
d=lambda x,y:x/y
e=lambda x,y:x//y
f=lambda x,y:x**y
g=lambda x,y:x%y

print("Calculation Menu")
print(" Press 1 for Sum")
print(" Press 2 for Subtraction")
print(" Press 3 for Product")
print(" Press 4 for Division")
print(" Press 5 for Floor Division")
print(" Press 6 for Power")
print(" Press 7 for modulus")

p=int(input("Enter your choice : "))

x=int(input("enter 1st number: "))
y=int(input("enter 2nd number: "))
if  p==1:
    print("sum =",a(x,y))
elif p==2:
    print("subtraction=",b(x,y))
elif p==3:
    print("product =",c(x,y))
elif p==4:
    print("division =",d(x,y))  
elif p==5:
    print("floor division =",e(x,y))
elif p==6:
    print("power =",f(x,y))
elif p==7:
    print("modulus =",g(x,y))             
else:
    print("  calculation exit. ")