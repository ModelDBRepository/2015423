import numpy as np
#import sys
import matplotlib.pyplot as plt
import os.path
import re

axixLabelSize = 20
ticksLabelSize = 20
titleFontSize = 28
mainTitleFontSize = 28



plt.figure(figsize=(27,9))
plt.subplots_adjust(hspace=0.5)


# -------------------------------------
# EXPERIMENTAL
# -------------------------------------

expVoltageFilename = 'trace_l23-06-13.res.6-tt6clu6_0.65+1_prova20122022.txt'

# VOLTAGE

time,volt = np.loadtxt(expVoltageFilename, usecols=(0,2),dtype=np.float64, unpack=True)

   
plt.subplot(221)
# title
plt.suptitle('SAP 4 weight: 650', fontsize=mainTitleFontSize,fontweight='bold')
      
# removes top and right frame 
for pos in ['right', 'top']:
  plt.gca().spines[pos].set_visible(False)


                
plt.plot(time/1000,volt,'k-',linewidth=1)
      
plt.gca().spines["left"].set_linewidth(2)
plt.gca().spines["bottom"].set_linewidth(2)
plt.gca().xaxis.set_tick_params(labelsize=ticksLabelSize)
plt.gca().yaxis.set_tick_params(labelsize=ticksLabelSize)                

plt.ylim([-75,40])
      
plt.xticks(weight='bold')
plt.yticks(np.arange(-75,50,25),weight='bold')
      
plt.ylabel('V (mV)',weight='bold',fontsize=axixLabelSize)
plt.title('in silico',fontsize=titleFontSize,fontweight='bold')


# ZOOM
plt.subplot(222)
      
# removes top and right frame 
for pos in ['right', 'top']:
  plt.gca().spines[pos].set_visible(False)

# select window width                
plt.plot(time[1840000:1875000]/1000,volt[1840000:1875000],'k-',linewidth=1)
      
plt.gca().spines["left"].set_linewidth(2)
plt.gca().spines["bottom"].set_linewidth(2)
plt.gca().xaxis.set_tick_params(labelsize=ticksLabelSize)
plt.gca().yaxis.set_tick_params(labelsize=ticksLabelSize)                

plt.ylim([-75,40])
      
plt.xticks(np.arange(184,188,0.5),weight='bold')
plt.yticks(np.arange(-75,50,25),weight='bold')
      
plt.ylabel('V (mV)',weight='bold',fontsize=axixLabelSize)
plt.title('in silico',fontsize=titleFontSize,fontweight='bold')





# -------------------------------------
# SIMULATION
# -------------------------------------


voltageFilename = '6_065_voltage_simulated.txt'
time,volt = np.loadtxt(voltageFilename, usecols=(0,1),dtype=np.float64, unpack=True)

spikeTimesFile = '6_065_t_spk_simulated.txt'
spikeTimes = np.loadtxt(spikeTimesFile, usecols=(0),dtype=np.float64, unpack=True)



# All time
#----------------
# selection of the time window for spikeTimes
mySpikeTimes = [i/1000 for i in spikeTimes if i< max(time) and i>min(time)]
# spikes to plot
myData= [[-20] for i in mySpikeTimes]

plt.subplot(223)

# removes top and right frame 
for pos in ['right', 'top']:
  plt.gca().spines[pos].set_visible(False)
          
plt.plot(time/1000,volt,'k-',linewidth=1)
plt.plot(mySpikeTimes,myData,'b|',markersize=100,linewidth=3,markeredgewidth=1)

plt.gca().spines["left"].set_linewidth(2)
plt.gca().spines["bottom"].set_linewidth(2)
plt.gca().xaxis.set_tick_params(labelsize=ticksLabelSize)
plt.gca().yaxis.set_tick_params(labelsize=ticksLabelSize)                

plt.axhline(y = -52, color = 'r', linestyle = '--',linewidth=1)  #700
plt.axhline(y = -65, color = 'r', linestyle = '-',linewidth=1)  #700
#plt.axvline(x=400, ymin=-55, ymax=-20, color='c', label='axvline - % of full height')

plt.ylim([-75,25])

plt.xticks(weight='bold')
plt.yticks(np.arange(-75,50,25),weight='bold')

plt.xlabel('time (s)',weight='bold',fontsize=axixLabelSize)
plt.ylabel('V (mV)',weight='bold',fontsize=axixLabelSize)
plt.title('model',fontsize=titleFontSize,fontweight='bold')


# time zoom      
#----------------

# selection of the time window for spikeTimes
mySpikeTimes = [i/1000 for i in spikeTimes if i< max(time[1840000:1875000]) and i>min(time[1840000:1875000])]
# spikes to plot
myData= [[-20] for i in mySpikeTimes]

plt.subplot(224)

# removes top and right frame 
for pos in ['right', 'top']:
  plt.gca().spines[pos].set_visible(False)
          
plt.plot(time[1840000:1875000]/1000,volt[1840000:1875000],'k-',linewidth=1)
plt.plot(mySpikeTimes,myData,'b|',markersize=100,linewidth=3,markeredgewidth=3)

plt.gca().spines["left"].set_linewidth(2)
plt.gca().spines["bottom"].set_linewidth(2)
plt.gca().xaxis.set_tick_params(labelsize=ticksLabelSize)
plt.gca().yaxis.set_tick_params(labelsize=ticksLabelSize)                

plt.axhline(y = -52, color = 'r', linestyle = '--',linewidth=1)  #700
plt.axhline(y = -65, color = 'r', linestyle = '-',linewidth=1)  #700

plt.ylim([-75,25])

plt.xticks(np.arange(184,188,0.5),weight='bold')
plt.yticks(np.arange(-75,50,25),weight='bold')   

plt.xlabel('time (s)',weight='bold',fontsize=axixLabelSize)
plt.ylabel('V (mV)',weight='bold',fontsize=axixLabelSize)
plt.title('model',fontsize=titleFontSize,fontweight='bold')






plt.savefig('figure8.png')
plt.close()