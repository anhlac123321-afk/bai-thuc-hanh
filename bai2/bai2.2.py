import math;
x1=int(input ("Con so gi day x1:"))
y1=int(input("Con so gi day y1:"))
x2=int(input("Con so gi day x2:"))
y2= int(input("Con so gi day y2:"))
d1 = (x2 - x1) * (x2 - x1);
d2 = (y2 - y1) * (y2 - y1);
res =math.sqrt(d1+d2)
print ("Tu do den do co khoang cach la:", res);
