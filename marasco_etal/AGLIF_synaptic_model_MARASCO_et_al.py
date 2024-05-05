import numpy as np
import matplotlib.pyplot as plt
from run_mds_nest import mds_nest_sim

fig = plt.figure()
p_time_stamps = []
p_membrane_voltage = []
p_time_stamps_ode = []
p_membrane_voltage_ode = []
n_time_stamps = []
n_membrane_voltage = []
Istim = [400, 500, 600, 700, 800, 1000, 1100]
sim_length=1000
campionamento=40
d_dt=0.1
i=1
Istim0 = 0
current = np.loadtxt('trace_l23-06-13.res.6-tt6clu2_0.65+1_prova06122022.txt') #[:10000,:]
# a, b , n_I_adapt, n_I_dep, n_spikes = mds_nest_sim('corrcost',current[:,1],d_dt, 'migliore')
# a = a + current[0,0]
# n_spikes = n_spikes + current[0,0]
a_ode, b_ode , n_I_adapt_ode, n_I_dep_ode, n_spikes_ode = mds_nest_sim('corrcost',current[:,1],d_dt, 'migliore_ode')
a_ode = a_ode + current[0,0]
n_spikes_ode = n_spikes_ode + current[0,0]
# p_time_stamps.append(a)
# p_membrane_voltage.append(b)
# p_time_stamps_ode.append(a_ode)
# p_membrane_voltage_ode.append(b_ode)
# lower = np.nonzero(current[:,0]>0)[0][0]
# upper = np.nonzero(current[:,0]>15000)[0][0]
# p_time_stamps_ode[i-1] = p_time_stamps_ode[i-1] * d_dt

plt.subplot(3,1,1)
plt.plot(current[:,0], current[:,2], 'k', label='NEURON')
# plt.xlim([75000, 95000])
plt.subplot(3,1,2)
plt.ylim([-80, 0])
# plt.xlim([75000, 95000])
# plt.plot(a,b, 'k', label='dora')
plt.plot(a_ode, b_ode, 'b', label='ode')

np.savetxt('membranepot_trace_l23-06-13.res.6-tt6clu2_0.65+1_prova06122022.txt', np.concatenate((a_ode.reshape(-1,1), b_ode.reshape(-1,1)), axis=1))
np.savetxt('spikes.txt', n_spikes_ode)

#plt.xlim([lower, upper])
plt.xlabel('Time (ms)')
for sp in n_spikes_ode:
    plt.axvline(sp, 0.5, 1, color='b')
# for sp in n_spikes:
#     plt.axvline(sp, color='k')

# plt.ylabel(str(Istim[i-1]/1000)+' nA',fontsize=7,rotation='horizontal', ha='right',va="center",weight='bold')
# #plt.ylim([-75, -30])
plt.subplot(3,1,3)
plt.plot(current[:,0], current[:,1])
#plt.xlim([lower, upper])
plt.xlim([75000, 95000])

plt.show()
plt.savefig('Model_traces_for_constant_current_injections_NEST.png')
