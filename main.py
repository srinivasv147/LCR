import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as manimation

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

def makePlot(A,B,w,t,eta,s):
	fig=plt.figure()
	fig.suptitle('current vs time', fontsize=14,fontweight='bold',family='serif')
	minTitle="eta="
	eta=eta[:3]#we only plot the first 3 etas for well defined plots.
	color=['red','blue','green']
	markers=['o','^','*']
	plts=[]
	etastr=[]
	i=0
	for e in eta:
		currentVal=current(A,B,w,t,e)
		newPlot,=plt.plot(t,currentVal,color=color[i],marker=markers[i],linewidth=3.3)
		minTitle+=str(e)+','
		plts.append(newPlot)
		etastr.append("eta="+str(e))
		i+=1
	plt.legend(plts,etastr,fontsize=14)
	ax = fig.add_subplot(111)
	ax.set_title(minTitle[:-1])
	ax.set_xlabel('time(sec)',fontsize=14,style='italic',family='serif')
	ax.set_ylabel('current(amp)',fontsize=14,style='italic',family='serif')
	# plt.show()
	plt.savefig(s+'.png')

def animate(A,B,w,t,eta):
	FFMpegWriter = manimation.writers['ffmpeg']
	metadata = dict(title='Current vs time', artist='Matplotlib',
                comment='Movie support!')
	writer = FFMpegWriter(fps=15, metadata=metadata)
	fig = plt.figure()
	l, = plt.plot([], [],'-o',lw=2)
	plt.xlim(0, 5)
	plt.ylim(-2, 2)
	with writer.saving(fig, "plot_130010033"+str(eta)+".mp4", 100):
		for time in t:
			# print current(A,B,w,time,eta)
			l.set_data(time,current(A,B,w,time,eta))
			writer.grab_frame() 

if __name__=='__main__':
	A=1
	B=1#we assume the constants to be 1
	w=12#the value of natural frequency which we consider
	t=np.linspace(0,1,num=100)#the range of time values
	eta=[0.5,1,1.5,2.5]
	makePlot(A,B,w,t,eta,'plots')
	animate(A,B,w,t,0.5)