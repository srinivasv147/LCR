import matplotlib.pyplot as plt
import numpy as np
A=1
B=1#we assume the constants to be 1
w=12#the value of natural frequency which we consider
t=np.linspace(0,10,num=100)#the range of time values

def current(A,B,w,t,eta):
	outVal=-1*eta*w*t
	if eta<1 and eta>0:
		inVal=t*np.sqrt(1-(eta)**2)*w
		return (A+B)*np.e**(outVal)*np.cos(inVal)
	elif eta==1:
		return (A+B)*np.e**(outVal)
	elif eta>1:
		innVal=t*np.sqrt(((eta)**2)-1)*w
		return np.e**(outVal)*((A*np.e**(innVal))+(B*np.e**(-1*innVal)))
	else:
		return
