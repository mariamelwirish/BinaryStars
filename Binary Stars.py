import matplotlib.pyplot as plt
import math
m1 = float(input("The mass of the first object in Kg: "))
m2 = float(input("The mass of the second object in Kg: "))
r1 = float(input("The radius of the first object in m: "))
r2 = float(input("The radius of the second object in m: "))
v1 = float(input("The velocity of the first object in m/s: "))
v2 = float(input("The velocity of the second object in m/s: "))
d  = float(input("The distance between the two objects in m: "))
D = d+r1+r2
d1 = (m2*D)//(m1+m2)
d2 = D-d1
pi = 3.14
G = 6.673*(10**-11)
M = G*(m1+m2)
AU = 1.5*10**11
a1 = 1/((2/D)-(v1**2/M)) #AU
a2 = 1/((2/D)-(v2**2/M)) 
alpha=1
x1data=[]
y1data=[]
x2data=[]
y2data=[]
E1 = (0.5*m1*(v1**2))-((G*m1*m2)//D)
E2 = (0.5*m2*(v2**2))-((G*m1*m2)//D)
mr = (m1*m2)//(m1+m2)
l1 = m1*v1*d1
l2 = m2*v2*d2
e1 =(abs(1+((2*E1*(l1**2))//(mr*((G*m1*m2)**2))))**0.5)
e2 =(abs(1+((2*E2*(l2**2))//(mr*((G*m1*m2)**2))))**0.5)

for alpha in range (1,361):
        r_change = a1*(1-e1**2)/(1+e1* math.cos(alpha))
        x1 = r_change * math.cos(alpha)+d1
        y1 = r_change * math.sin(alpha)
        
        x1data.append(x1)
        y1data.append(y1)   
        
        b_change = (a2*(1-e2**2)/(1+e2*math.cos(alpha)))
        x2 = b_change * math.cos(alpha)+d2
        y2 = b_change * math.sin(alpha)
      
        x2data.append(x2)
        y2data.append(y2)
        alpha+=1
                                                                                                                                      
        plt.plot(x1data,y1data,'b')
        plt.plot(x2data,y2data,'g')


        plt.show()
