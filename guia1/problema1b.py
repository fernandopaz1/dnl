import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *



################################################################################################

#          Grafico del campo vector

################################################################################################


print("El campo vector es:  4x**2-16")


def f(t): return (2*t-4)*(2*t+4)

x=np.linspace(-4,4,1000)



plt.figure(1)
a_pos,=plt.plot(x,f(x),label='Campo vector')
variable,=plt.plot(x,np.zeros(len(x)),label='x(t)')
plt.arrow(3, 0, 1, 0, shape='full', lw=0, length_includes_head=True, head_width=1.5)
plt.arrow(0, 0, -1, 0, shape='full', lw=0, length_includes_head=True, head_width=1.25)
plt.arrow(-2.5, 0, 1, 0, shape='full', lw=0, length_includes_head=True, head_width=1.5)
plt.legend(loc='best')
plt.xlabel("x(t)")
plt.ylabel("f(x)")
plt.show(block=True)


################################################################################################

#          Resolucion numerica de los problemas

#		Metodo de Euler		
################################################################################################




t=np.linspace(0,0.5,1000)
h=t[1]-t[0]
sol1=np.zeros(len(t))
sol2=np.zeros(len(t))
sol3=np.zeros(len(t))
sol1[0]=0
sol2[0]=-3
sol3[0]=2.00000000001


for i in range(0,len(t)-1):
	sol1[i+1]=sol1[i]+h*f(sol1[i])
	sol2[i+1]=sol2[i]+h*f(sol2[i])
	sol3[i+1]=sol3[i]+h*f(sol3[i])



plt.figure(3)
a_pos,=plt.plot(t,sol1,label='x(t=0)=0')
a_neg,=plt.plot(t,sol2,label='x(t=0)=-3')
plt.legend(loc='best')
#plt.title('a>0')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show(block=True)


plt.figure(2)
cer,=plt.plot(t,sol3,label='x(t=0)=3')
plt.legend(loc='best')
#plt.title('a>0')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show(block=True)

