side1=int(input("Enter length of first side:"))
side2=int(input("Enter lenth of second side"))
side3=int(input("enter length of third side"))
if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
    print("yes")
else:
    print("no")