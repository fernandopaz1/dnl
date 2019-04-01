import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *



################################################################################################

#          Grafico del campo vector

################################################################################################


print("El campo vector es:  a*x")
a1=1
a2=-1

def f(a,t): return a*t

x=np.linspace(-10,10,1000)



plt.figure(1)
a_pos,=plt.plot(x,f(a1,x),label='Campo vector a>0')
variable,=plt.plot(x,f(0,x),label='x(t)')
plt.arrow(2.5, f(0,2.5), 3, f(0,3), shape='full', lw=0, length_includes_head=True, head_width=1)
plt.arrow(-2.5, f(0,-2.5), -3, f(0,-3), shape='full', lw=0, length_includes_head=True, head_width=1)
plt.legend(loc='best')
plt.xlabel("x(t)")
plt.ylabel("a*x")
plt.show(block=True)


plt.figure(2)
a_pos,=plt.plot(x,f(a2,x),label='Campo vector a<0')
variable,=plt.plot(x,f(0,x),label='x(t)')
plt.arrow(5, f(0,5), -3, f(0,3), shape='full', lw=0, length_includes_head=True, head_width=1)
plt.arrow(-5, f(0,-5), +3, f(0,+3), shape='full', lw=0, length_includes_head=True, head_width=1)
plt.legend(loc='best')
plt.xlabel("x(t)")
plt.ylabel("a*x")
plt.show(block=True)


################################################################################################

#          Resolucion numerica de los problemas

#		Metodo de Euler		
################################################################################################




######################################################################
#                        a>0
######################################################################
t=np.linspace(0,2,1000)
h=t[1]-t[0]
sol1=np.zeros(len(t))
sol2=np.zeros(len(t))
sol1[0]=1
sol2[0]=-1


for i in range(0,len(t)-1):
	sol1[i+1]=sol1[i]+h*f(a1,sol1[i])
	sol2[i+1]=sol2[i]+h*f(a1,sol2[i])



plt.figure(3)
a_pos,=plt.plot(t,sol1,label='x(t=0)=1')
cer,=plt.plot(t,np.zeros(len(t)),label='x(t=0)=0')
a_neg,=plt.plot(t,sol2,label='x(t=0)=-1')
plt.legend(loc='best')
plt.title('a>0')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show(block=True)

######################################################################
#                        a<0
######################################################################
sol1=np.zeros(len(t))
sol2=np.zeros(len(t))
sol1[0]=1
sol2[0]=-1


for i in range(0,len(t)-1):
	sol1[i+1]=sol1[i]+h*f(a2,sol1[i])
	sol2[i+1]=sol2[i]+h*f(a2,sol2[i])



plt.figure(1)
a_pos,=plt.plot(t,sol1,label='x(t=0)=1')
cer,=plt.plot(t,np.zeros(len(t)),label='x(t=0)=0')
a_neg,=plt.plot(t,sol2,label='x(t=0)=-1')
plt.legend(loc='best')
plt.title('a<0')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show(block=True)


