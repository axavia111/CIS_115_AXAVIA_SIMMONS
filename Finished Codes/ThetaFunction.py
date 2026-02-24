#This program finds the angle theta



from math import atan2
x = float(input("Enter a integer value: "))
y = float(input("Enter a integer value: "))




def RightTriangle():
  
    sum = (x * x) + (y * y)

    c = sum ** .5
    angle_theta()
    return


def angle_theta():
    
    sum = atan2(y,x)

    angle = sum * float(180 / 3.145)
    print(f"The angle theta is: {angle:,.2f}")
    
RightTriangle()