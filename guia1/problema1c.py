import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *



################################################################################################

#          Grafico del campo vector

################################################################################################


print("El campo vector es:  x*(1-x**2)")


def f(t): return t*(1-t**2)

x=np.linspace(-1.75,0.5,1000)



plt.figure(1)
a_pos,=plt.plot(x,f(x),label='Campo vector')
variable,=plt.plot(x,np.zeros(len(x)),label='x(t)')
plt.arrow(2, 0, -1, 0, shape='full', lw=0, length_includes_head=True, head_width=0.1)
plt.arrow(0, 0, -1, 0, shape='full', lw=0, length_includes_head=True, head_width=0.1)
plt.arrow(0, 0, 1, 0, shape='full', lw=0, length_includes_head=True, head_width=0.1)
plt.arrow(-2, 0, 1, 0, shape='full', lw=0, length_includes_head=True, head_width=0.1)
plt.legend(loc='best')
plt.xlabel("x(t)")
plt.ylabel("f(x)")
plt.show(block=True)


################################################################################################

#          Resolucion numerica de los problemas

#		Metodo de Euler		
################################################################################################




t=np.linspace(0,3,1000)
h=t[1]-t[0]
sol1=np.zeros(len(t))
sol2=np.zeros(len(t))
sol3=np.zeros(len(t))
sol4=np.zeros(len(t))
sol1[0]=-2
sol2[0]=-0.5
sol3[0]=0.5
sol4[0]=2


for i in range(0,len(t)-1):
	#sol1[i+1]=sol1[i]+h*f(sol1[i])
	sol2[i+1]=sol2[i]+h*f(sol2[i])
	sol3[i+1]=sol3[i]+h*f(sol3[i])
	sol4[i+1]=sol4[i]+h*f(sol4[i])



plt.figure(3)
a_pos,=plt.plot(t,sol1,label='x(t=0)=-2')
a_neg,=plt.plot(t,sol2,label='x(t=0)=-0.5')
cer,=plt.plot(t,sol3,label='x(t=0)=0.5')
cer,=plt.plot(t,sol4,label='x(t=0)=2')
plt.legend(loc='best')
#plt.title('a>0')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show(block=True)


#plt.figure(2)
#cer,=plt.plot(t,sol3,label='x(t=0)=3')
#plt.legend(loc='best')
#plt.title('a>0')
#plt.xlabel("t")
#plt.ylabel("x(t)")
#plt.show(block=True)
