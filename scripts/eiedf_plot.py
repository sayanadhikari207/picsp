import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pylab import *
import cmath
# numerical data file
# CAUTION!! Run the eiedf_data_gen.sh file first
DIR="../output/phase_space"
DATA = "Ion"
nTimeSteps = 20000 # Put the value at which stage you want the EEDF/IEDF
# numerical data file
charge_electron = 1.6e-19

if DATA=="Ion":
    filename1=DIR+'/i1_%d'%nTimeSteps+'.dat'
    filename2=DIR+'/i2_%d'%nTimeSteps+'.dat'
    funcName = "IEDF"
    massI1 =1.673e-27
    massI2 =6.6335209E-26 #Argon
    KE_in_EV_coeff1 = 0.5*massI1/charge_electron
    KE_in_EV_coeff2 = 0.5*massI2/charge_electron
    dataI1x,dataI1v = np.loadtxt(filename1, unpack=True)
    dataI2x,dataI2v = np.loadtxt(filename2, unpack=True)
elif DATA=="Electron":
    filename1=DIR+'/e%d'%nTimeSteps+'.dat'
    funcName = "EEDF"
    mass = 9.1E-31 #electron
    KE_in_EV_coeff = 0.5*mass/charge_electron
    datax,datav = np.loadtxt(filename1, unpack=True)

else:
    raise Exception("Error in input DATA TYPE")




#velocity data within a range
range1 = np.array([0.0010,0.0015,0.0019])
range2 = np.array([0.0011,0.0016,0.0020])

#disp(range2[2])
#Empty data array to store velocity data for a location range

if DATA=="Ion":
    data_loc1I1 = np.empty([len(dataI1x), 1], dtype=float)
    data_loc1I1[:] = np.NaN
    data_loc2I1 = np.empty([len(dataI1x), 1], dtype=float)
    data_loc2I1[:] = np.NaN
    data_loc3I1 = np.empty([len(dataI1x), 1], dtype=float)
    data_loc3I1[:] = np.NaN
    
    data_loc1I2 = np.empty([len(dataI2x), 1], dtype=float)
    data_loc1I2[:] = np.NaN
    data_loc2I2 = np.empty([len(dataI2x), 1], dtype=float)
    data_loc2I2[:] = np.NaN
    data_loc3I2 = np.empty([len(dataI2x), 1], dtype=float)
    data_loc3I2[:] = np.NaN
    #storing data for the range given
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    for i in range(len(dataI1x)):
        if (dataI1x[i] >= range1[0]) and (dataI1x[i] <= range2[0]):
            data_loc1I1[j]= dataI1v[i]
            j = j+1
        elif (dataI1x[i] >= range1[1]) and (dataI1x[i] <= range2[1]):
            data_loc2I1[k]= dataI1v[i]
            k = k+1
        elif (dataI1x[i] >= range1[2]) and (dataI1x[i] <= range2[2]):
            data_loc3I1[l]= dataI1v[i]
            l = l+1
        elif (dataI2x[i] >= range1[0]) and (dataI2x[i] <= range2[0]):
            data_loc1I2[j]= dataI2v[i]
            m = m+1
        elif (dataI2x[i] >= range1[1]) and (dataI2x[i] <= range2[1]):
            data_loc2I2[k]= dataI2v[i]
            n = n+1
        elif (dataI2x[i] >= range1[2]) and (dataI2x[i] <= range2[2]):
            data_loc3I2[l]= dataI2v[i]
            o = o+1
        else:
            None
    data_EV_loc1I1 = KE_in_EV_coeff1*data_loc1I1*data_loc1I1
    data_EV_loc2I1 = KE_in_EV_coeff1*data_loc2I1*data_loc2I1
    data_EV_loc3I1 = KE_in_EV_coeff1*data_loc3I1*data_loc3I1
    
    data_EV_loc1I2 = KE_in_EV_coeff2*data_loc1I2*data_loc1I2
    data_EV_loc2I2 = KE_in_EV_coeff2*data_loc2I2*data_loc2I2
    data_EV_loc3I2 = KE_in_EV_coeff2*data_loc3I2*data_loc3I2
elif DATA=="Electron":
    data_loc1 = np.empty([len(datax), 1], dtype=float)
    data_loc1[:] = np.NaN
    data_loc2 = np.empty([len(datax), 1], dtype=float)
    data_loc2[:] = np.NaN
    data_loc3 = np.empty([len(datax), 1], dtype=float)
    data_loc3[:] = np.NaN
    #storing data for the range given
    j = 0
    k = 0
    l = 0
    for i in range(len(datax)):
        if (datax[i] >= range1[0]) and (datax[i] <= range2[0]):
            data_loc1[j]= datav[i]
            j = j+1
        elif (datax[i] >= range1[1]) and (datax[i] <= range2[1]):
            data_loc2[k]= datav[i]
            k = k+1
        elif (datax[i] >= range1[2]) and (datax[i] <= range2[2]):
            data_loc3[l]= datav[i]
            l = l+1
        else:
            None
    data_EV_loc1 = KE_in_EV_coeff*data_loc1*data_loc1
    data_EV_loc2 = KE_in_EV_coeff*data_loc2*data_loc2
    data_EV_loc3 = KE_in_EV_coeff*data_loc3*data_loc3
else:
    raise Exception("Error in input DATA TYPE")
#Conversion of velocities to energy
#data in eV


if DATA=="Ion":
    fig, (ax1,ax2,ax3) = plt.subplots(3,1)
    plt.rcParams["font.size"] = "12"
    plt.rcParams["font.family"] = "Helvetica"
    sns.distplot(data_EV_loc1I1[:], hist=False, kde=True, color = 'darkblue',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax1)
    sns.distplot(data_EV_loc1I2[:], hist=False, kde=True, color = 'darkviolet',
    hist_kws={'edgecolor':'black'},
    kde_kws={'shade': True, 'linewidth': 2},ax=ax1)
    ax1.set_xlabel('Energy (eV)')
    ax1.set_ylabel('A.U.')
    #ax1.set_xlim(-10,50)
    ax1.legend(['Location: %1.4f'%range1[0]+'-%1.4f'%range2[0]])
    ax1.set_title(DATA+' Energy Distribution Function('+funcName+')')

    sns.distplot(data_EV_loc2I1[:], hist=False, kde=True, color = 'red',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax2)
    sns.distplot(data_EV_loc2I2[:], hist=False, kde=True, color = 'lightcoral',
    hist_kws={'edgecolor':'black'},
    kde_kws={'shade': True, 'linewidth': 2},ax=ax2)
    ax2.set_xlabel('Energy (eV)')
    ax2.set_ylabel('A.U.')

    #ax2.set_xlim(-10,50)
    ax2.legend(['Location: %1.4f'%range1[1]+'-%1.4f'%range2[1]])

    sns.distplot(data_EV_loc3I1[:], hist=False, kde=True, color = 'lime',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax3)
    sns.distplot(data_EV_loc3I2[:], hist=False, kde=True, color = 'darkgreen',
    hist_kws={'edgecolor':'black'},
    kde_kws={'shade': True, 'linewidth': 2},ax=ax3)
    ax3.set_xlabel('Energy (eV)')
    ax3.set_ylabel('A.U.')
    #ax3.set_xlim(-10,50)
    ax3.legend(['Location: %1.4f'%range1[2]+'-%1.4f'%range2[2]])
    #ax3.set_xlim(0,100)

    fig, ax1 = plt.subplots(1,1)
    plt.rcParams["font.size"] = "12"
    plt.rcParams["font.family"] = "Helvetica"
    sns.distplot(data_EV_loc1I1[:], hist=False, kde=True, color = 'darkblue',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax1)
    sns.distplot(data_EV_loc2I1[:], hist=False, kde=True, color = 'red',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax1)
    sns.distplot(data_EV_loc3I1[:], hist=False, kde=True, color = 'green',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax1)
    ax1.grid(True)
    ax1.set_xlabel('Energy (eV)')

    #ax1.set_xlim(-10,50)
    ax1.set_ylabel('A.U.')
    ax1.set_title(DATA+' Energy Distribution Function('+funcName+')')
    ax1.legend(['Location: %1.4f'%range1[0]+'-%1.4f'%range2[0],'Location: %1.4f'%range1[1]+'-%1.4f'%range2[1],'Location: %1.4f'%range1[2]+'-%1.4f'%range2[2]])

    plt.show()
elif DATA=="Electron":
    fig, (ax1,ax2,ax3) = plt.subplots(3,1)
    plt.rcParams["font.size"] = "12"
    plt.rcParams["font.family"] = "Helvetica"
    sns.distplot(data_EV_loc1[:], hist=True, kde=True, color = 'darkblue',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax1)
    ax1.set_xlabel('Energy (eV)')
    ax1.set_ylabel('A.U.')
    #ax1.set_xlim(-10,50)
    ax1.legend(['Location: %1.4f'%range1[0]+'-%1.4f'%range2[0]])
    ax1.set_title(DATA+' Energy Distribution Function('+funcName+')')

    sns.distplot(data_EV_loc2[:], hist=True, kde=True, color = 'red',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax2)
    ax2.set_xlabel('Energy (eV)')
    ax2.set_ylabel('A.U.')

    #ax2.set_xlim(-10,50)
    ax2.legend(['Location: %1.4f'%range1[1]+'-%1.4f'%range2[1]])

    sns.distplot(data_EV_loc3[:], hist=True, kde=True, color = 'green',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax3)
    ax3.set_xlabel('Energy (eV)')
    ax3.set_ylabel('A.U.')
    #ax3.set_xlim(-10,50)
    ax3.legend(['Location: %1.4f'%range1[2]+'-%1.4f'%range2[2]])
    #ax3.set_xlim(0,100)

    fig, ax1 = plt.subplots(1,1)
    plt.rcParams["font.size"] = "12"
    plt.rcParams["font.family"] = "Helvetica"
    sns.distplot(data_EV_loc1[:], hist=False, kde=True, color = 'darkblue',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax1)
    sns.distplot(data_EV_loc2[:], hist=False, kde=True, color = 'red',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax1)
    sns.distplot(data_EV_loc3[:], hist=False, kde=True, color = 'green',
                 hist_kws={'edgecolor':'black'},
                 kde_kws={'shade': True, 'linewidth': 2},ax=ax1)
    ax1.grid(True)
    ax1.set_xlabel('Energy (eV)')

    #ax1.set_xlim(-10,50)
    ax1.set_ylabel('A.U.')
    ax1.set_title(DATA+' Energy Distribution Function('+funcName+')')
    ax1.legend(['Location: %1.4f'%range1[0]+'-%1.4f'%range2[0],'Location: %1.4f'%range1[1]+'-%1.4f'%range2[1],'Location: %1.4f'%range1[2]+'-%1.4f'%range2[2]])

    plt.show()
else:
    raise Exception("Error in input DATA TYPE")
