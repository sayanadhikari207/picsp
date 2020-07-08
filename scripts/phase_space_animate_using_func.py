import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pylab import *
import matplotlib.animation as animation

nTimeSteps = 20000 #copy it from .ini file
save_anim = True
onlyshow_anim = False
interval = 0.1#in seconds
#dt = 1.117748050647400e-08
#data_num = np.arange(start=0, stop=nTimeSteps, step=1, dtype=int)
#time = data_num*dt*10000
data_num = np.arange(start=0, stop=nTimeSteps, step=50, dtype=int)
# numerical data file
DIR ="../output/phase_space"
#DIR ="acc1/foc1/dispersion/vspace"

fig,(ax1,ax2) = plt.subplots(2,1,figsize=(10, 9))

#from mpl_toolkits.axes_grid1 import make_axes_locatable
#
#div = make_axes_locatable(ax)
#cax = div.append_axes('right', '5%', '5%')


def animate(i):
    filename1=DIR+'/i1_%d'%data_num[i]+'.dat'
    filename2=DIR+'/i2_%d'%data_num[i]+'.dat'
    datax1,datav1 = np.loadtxt(filename1, unpack=True)
    datax2,datav2 = np.loadtxt(filename2, unpack=True)

    filename3=DIR+'/e%d'%data_num[i]+'.dat'
    datax3,datav3 = np.loadtxt(filename3, unpack=True)
    
    ax1.cla()
    img1 = ax1.scatter(datax1,datav1,s=1,marker='.',color='b',alpha=1.0,label='Ion1')
    img2 = ax1.scatter(datax2,datav2,s=1,marker='.',color='k',alpha=1.0,label='Ion2')
    ax1.set_title('TimeSteps = %d'%i+'\nIon Phase Space')
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$v_x$")
    ax1.legend()
    
    ax2.cla()
    img3 = ax2.scatter(datax3,datav3,s=1,marker='.',color='b',alpha=1.0)
    ax2.set_title('Electron Phase Space')
    ax2.set_xlabel("$x$")
    ax2.set_ylabel("$V_x$")
    


ani = animation.FuncAnimation(fig,animate,frames=len(data_num),interval=interval*1e+3,blit=False)


#for i in range(data_num.size):
##    filename1=DIR+'/iedf_vx_x_%d'%i+'.txt'
#    filename=DIR+'/iedf_vx_x_%d'%data_num[i]+'.txt'
#    data = np.loadtxt(filename, delimiter="\t", skiprows=2, usecols=[0,2])
#    datax = data[:,0]
#    datav = data[:,1]
#
#    figure(1)
#    plt.scatter(datax,datav,s=1,marker='.',color='b',alpha=0.6)
#    plt.xlabel("$z$")
#    plt.ylabel("$v_z$")
##    plt.title('Time = %3.1e'%time[0]+' s')
#    plt.title('TimeSteps = %d'%i)
#    plt.tight_layout()
   
    
if(save_anim == True):
#    plt.show()
    ani.save('animation_phase_space.gif',writer='imagemagick')
else:
    if (onlyshow_anim == True):
        plt.show()
##        plt.pause(0.1)
##        plt.clf()
#    else:
#        for i in range(data_num):
#            animate(i)



