
#Importing libraries
import os
import datetime
from datetime import datetime
import matplotlib.pyplot as plt
os.environ["CDF_LIB"] = "C:/Program Files/CDF_Distribution/cdf38_1-dist/lib"
from spacepy import pycdf
import numpy as np
import math


#Reading Data

#Magnetic field
cdf = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/tha_l2_fgm_20160103_v01.cdf')
Bdata_THA = cdf['tha_fgs_gsm'][...]
Btime_THA = cdf['tha_fgs_time'][...]


cdf1 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/thd_l2_fgm_20160103_v01.cdf')
Bdata_THD = cdf1['thd_fgs_gsm'][...]
Btime_THD = cdf1['thd_fgs_time'][...]


cdf2 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/the_l2_fgm_20160103_v01.cdf')
Bdata_THE = cdf2['the_fgs_gsm'][...]
Btime_THE = cdf2['the_fgs_time'][...]


#Position Data
cdf3 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/tha_l1_state_20160103_v01.cdf')
PosData_THA = cdf3['tha_pos_gsm'][...]
PosTime_THA = cdf3['tha_state_time'][...]


cdf4 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/thd_l1_state_20160103_v01.cdf')
PosData_THD = cdf4['thd_pos_gsm'][...]
PosTime_THD = cdf4['thd_state_time'][...]


cdf5 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/the_l1_state_20160103_v01.cdf')
PosData_THE = cdf5['the_pos_gsm'][...]
PosTime_THE = cdf5['the_state_time'][...]


#GMOM Data (ion temperature data)
cdf6 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/tha_l2_gmom_20160103_v01.cdf')
IonTempData_THA = cdf6['tha_ptirf_magt3'][...]
IonGMOMTime_THA = cdf6['tha_ptirf_time'][...]


cdf7 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/the_l2_gmom_20160103_v01.cdf')
IonTempData_THE = cdf7['the_ptirf_magt3'][...]
IonGMOMTime_THE = cdf7['the_ptirf_time'][...]


cdf8 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/thd_l2_gmom_20160103_v01.cdf')
IonTempData_THD = cdf8['thd_ptirf_magt3'][...]
IonGMOMTime_THD = cdf8['thd_ptirf_time'][...]


#MOM Data (electron temperature, electron density, ion velocity data)

#electron temperature
cdf9 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/tha_l2_mom_20160103_v01.cdf')
ElectTempData_THA = cdf9['tha_peem_t3_mag'][...]
ElectMOMTime_THA = cdf9['tha_peem_time'][...]


cdf10 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/thd_l2_mom_20160103_v01.cdf')
ElectTempData_THD = cdf10['thd_peem_t3_mag'][...]
ElectMOMTime_THD = cdf10['thd_peem_time'][...]


cdf11 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/the_l2_mom_20160103_v01.cdf')
ElectTempData_THE = cdf11['the_peem_t3_mag'][...]
ElectMOMTime_THE = cdf11['the_peem_time'][...]


#electron density
cdf12 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/tha_l2_mom_20160103_v01.cdf')
ElectDensData_THA = cdf12['tha_peem_density'][...]

cdf13 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/thd_l2_mom_20160103_v01.cdf')
ElectDensData_THD = cdf13['thd_peem_density'][...]

cdf14 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/the_l2_mom_20160103_v01.cdf')
ElectDensData_THE = cdf14['the_peem_density'][...]

#ion velocity 
cdf15 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/tha_l2_mom_20160103_v01.cdf')
VelIon_THA = cdf15['tha_peim_velocity_gsm'][...]
IonMOMTime_THA = cdf15['tha_peim_time'][...]


#Entering time constraints that are associated with time period of plasma injection
s1 = 8274
s2 = 6911
s3 = 5766
s4 = 8312
s5 = 6584
s6 = 5840
s7 = 8307
s8 = 6869
s9 = 5829
s10 = 401

#Presettling the arrays
ion_tperp1_THA = np.zeros (1247)
ion_tperp2_THA = np.zeros (1247)
ion_tpar_THA = np.zeros (1247)
ion_time_THA = np.zeros (1247)
B_X_THA = np.zeros (1247)
B_Y_THA = np.zeros (1247)
B_Z_THA = np.zeros (1247)
B_time_THA  = np.zeros (1247)
electron_tperp1_THA = np.zeros (1247)
electron_tperp2_THA = np.zeros (1247)
electron_tpar_THA = np.zeros (1247)
density_THA = np.zeros (1247)
mom_electron_time_THA = np.zeros (1247)
velocity_X_THA = np.zeros (1247)
mom_ion_time_THA = np.zeros (1247)

for i in range (1247):
        ion_tperp1_THA [i] = IonTempData_THA[s4,0]
        ion_tperp2_THA [i]  = IonTempData_THA  [s4,1]
        ion_tpar_THA [i]  = IonTempData_THA [s4,2]
        ion_time_THA [i]  = IonGMOMTime_THA [s4];

       
        B_X_THA [i]  = Bdata_THA[s1,0]
        B_Y_THA [i]  = Bdata_THA[s1,1]
        B_Z_THA [i]  = Bdata_THA[s1,2]
        B_time_THA [i]  = Btime_THA[s1]

        s4 = s4 + 1
        s1 = s1 + 1

        electron_tperp1_THA [i] = ElectTempData_THA [s7,0]
        electron_tperp2_THA [i] = ElectTempData_THA  [s7,1]
        electron_tpar_THA [i] = ElectTempData_THA  [s7,2]
        density_THA [i] = ElectDensData_THA [s7]
        mom_electron_time_THA [i] = ElectMOMTime_THA[s7]
        
        velocity_X_THA [i] = VelIon_THA [s7,0]
        mom_ion_time_THA [i] = IonMOMTime_THA [s7]

        s7 = s7 + 1

#Presettling the arrays
ion_tperp1_THD = np.zeros (1141)
ion_tperp2_THD = np.zeros (1141)
ion_tpar_THD = np.zeros (1141)
ion_time_THD = np.zeros (1141)
B_X_THD = np.zeros (1141)
B_Y_THD = np.zeros (1141)
B_Z_THD = np.zeros (1141)
B_time_THD  = np.zeros (1141)
electron_tperp1_THD = np.zeros (1141)
electron_tperp2_THD = np.zeros (1141)
electron_tpar_THD = np.zeros (1141)
density_THD = np.zeros (1141)
mom_electron_time_THD = np.zeros (1141)
velocity_X_THD = np.zeros (1141)
mom_ion_time_THD = np.zeros (1141)

for i in range (1141):
        ion_tperp1_THD [i] = IonTempData_THD[s5,0]
        ion_tperp2_THD [i]  = IonTempData_THD  [s5,1]
        ion_tpar_THD [i]  = IonTempData_THD [s5,2]
        ion_time_THD [i]  = IonGMOMTime_THD [s5];

       
        B_X_THD [i]  = Bdata_THD[s2,0]
        B_Y_THD [i]  = Bdata_THD[s2,1]
        B_Z_THD [i]  = Bdata_THD[s2,2]
        B_time_THD [i]  = Btime_THD[s2]

        s2 = s2 + 1
        s5 = s5 + 1

        electron_tperp1_THD [i] = ElectTempData_THD [s8,0]
        electron_tperp2_THD [i] = ElectTempData_THD  [s8,1]
        electron_tpar_THD [i] = ElectTempData_THD  [s8,2]
        density_THD [i] = ElectDensData_THD [s8]
        mom_electron_time_THD [i] = ElectMOMTime_THD[s8]
        

        s8 = s8 + 1

#Presettling the arrays
ion_tperp1_THE = np.zeros (876)
ion_tperp2_THE = np.zeros (876)
ion_tpar_THE = np.zeros (876)
ion_time_THE = np.zeros (876)
B_X_THE = np.zeros (876)
B_Y_THE = np.zeros (876)
B_Z_THE = np.zeros (876)
B_time_THE  = np.zeros (876)
electron_tperp1_THE = np.zeros (876)
electron_tperp2_THE = np.zeros (876)
electron_tpar_THE = np.zeros (876)
density_THE = np.zeros (876)
mom_electron_time_THE = np.zeros (876)
velocity_X_THE = np.zeros (876)
mom_ion_time_THE = np.zeros (876)


for i in range (876):
        ion_tperp1_THE [i] = IonTempData_THE[s6,0]
        ion_tperp2_THE [i]  = IonTempData_THE  [s6,1]
        ion_tpar_THE [i]  = IonTempData_THE [s6,2]
        ion_time_THE [i]  = IonGMOMTime_THE [s6];

       
        B_X_THE [i]  = Bdata_THE[s3,0]
        B_Y_THE [i]  = Bdata_THE[s3,1]
        B_Z_THE [i]  = Bdata_THE[s3,2]
        B_time_THE [i]  = Btime_THE[s3]

        s3 = s3 + 1
        s6 = s6 + 1

        electron_tperp1_THE [i] = ElectTempData_THE [s9,0]
        electron_tperp2_THE [i] = ElectTempData_THE  [s9,1]
        electron_tpar_THE [i] = ElectTempData_THE  [s9,2]
        density_THE [i] = ElectDensData_THE [s9]
        mom_electron_time_THE [i] = ElectMOMTime_THE[s9]
        

        s9 = s9 + 1
 
        
 #Presettling the arrays
state_X_THA = np.zeros (60)
state_Z_THA = np.zeros (60)
state_X_THD = np.zeros (60)
state_Z_THD = np.zeros (60)
state_X_THE = np.zeros (60)
state_Z_THE = np.zeros (60)
state_time = np.zeros (60)

for i in range (60):
        state_X_THA [i] = PosData_THA [s10,0]
        state_Z_THA [i] = PosData_THA [s10,2]
        
        state_X_THD [i] = PosData_THD [s10,0]
        state_Z_THD [i] = PosData_THD[s10,2]

        state_X_THE [i] = PosData_THE [s10,0]
        state_Z_THE [i] = PosData_THE [s10,2]

        state_time [i] = PosTime_THA [s10]
        s10 = s10+1



#Interpolation

# Magnetic Field
B_X_THD_interp  = np.interp(B_time_THA, B_time_THD, B_X_THD)
B_Y_THD_interp  = np.interp(B_time_THA,B_time_THD, B_Y_THD)
B_Z_THD_interp  = np.interp(B_time_THA,B_time_THD, B_Z_THD)

B_X_THE_interp  = np.interp(B_time_THA,B_time_THE, B_X_THE)
B_Y_THE_interp  = np.interp(B_time_THA,B_time_THE, B_Y_THE)
B_Z_THE_interp  = np.interp(B_time_THA,B_time_THE, B_Z_THE)

#Position
state_X_THA_interp  = np.interp(B_time_THA,state_time, state_X_THA)
state_Z_THA_interp  = np.interp(B_time_THA,state_time, state_Z_THA)

state_X_THD_interp  = np.interp(B_time_THA,state_time, state_X_THD)
state_Z_THD_interp  = np.interp(B_time_THA,state_time, state_Z_THD)

state_X_THE_interp  = np.interp(B_time_THA,state_time, state_X_THE)
state_Z_THE_interp  = np.interp(B_time_THA,state_time, state_Z_THE)

#Ion Temperature GMOM
ion_tperp1_THA_interp = np.interp(B_time_THA,ion_time_THA, ion_tperp1_THA)
ion_tperp2_THA_interp = np.interp(B_time_THA,ion_time_THA, ion_tperp2_THA)
ion_tpar_THA_interp = np.interp(B_time_THA,ion_time_THA, ion_tpar_THA)

ion_tperp1_THD_interp = np.interp(B_time_THA,ion_time_THD, ion_tperp1_THD)
ion_tperp2_THD_interp = np.interp(B_time_THA,ion_time_THD, ion_tperp2_THD)
ion_tpar_THD_interp = np.interp(B_time_THA,ion_time_THD, ion_tpar_THD)
    
ion_tperp1_THE_interp = np.interp(B_time_THA,ion_time_THE, ion_tperp1_THE)
ion_tperp2_THE_interp = np.interp(B_time_THA,ion_time_THE, ion_tperp2_THE)
ion_tpar_THE_interp = np.interp(B_time_THA,ion_time_THE, ion_tpar_THE)

#Electron Temperature MOM
electron_tperp1_THA_interp = np.interp(B_time_THA,mom_electron_time_THA, electron_tperp1_THA)
electron_tperp2_THA_interp = np.interp(B_time_THA,mom_electron_time_THA, electron_tperp2_THA)
electron_tpar_THA_interp = np.interp(B_time_THA,mom_electron_time_THA, electron_tpar_THA)

electron_tperp1_THD_interp = np.interp(B_time_THA,mom_electron_time_THD, electron_tperp1_THD)
electron_tperp2_THD_interp = np.interp(B_time_THA,mom_electron_time_THD, electron_tperp2_THD)
electron_tpar_THD_interp = np.interp(B_time_THA,mom_electron_time_THD, electron_tpar_THD)

electron_tperp1_THE_interp = np.interp(B_time_THA,mom_electron_time_THE, electron_tperp1_THE)
electron_tperp2_THE_interp = np.interp(B_time_THA,mom_electron_time_THE, electron_tperp2_THE)
electron_tpar_THE_interp = np.interp(B_time_THA,mom_electron_time_THE, electron_tpar_THE)

#Electron Density MOM
density_THA_interp = np.interp(B_time_THA,mom_electron_time_THA, density_THA)
density_THD_interp = np.interp(B_time_THA,mom_electron_time_THD, density_THD)
density_THE_interp = np.interp(B_time_THA,mom_electron_time_THE, density_THE)
    
#Ion velocity MOM
velocity_X_THA_interp = np.interp(B_time_THA, mom_ion_time_THA, velocity_X_THA)



#Calculating physical parameters

#Current Density and Divergence

#Presettling the arrays
dBz_AE = np.zeros (1247)
dBx_AE = np.zeros (1247)
dBz_DE = np.zeros (1247)
dBx_DE = np.zeros (1247)
dz_AE = np.zeros (1247)
dx_AE = np.zeros (1247)
dz_DE  = np.zeros (1247)
dx_DE = np.zeros (1247)
dBz_dx  = np.zeros (1247)
dBx_dz = np.zeros (1247)
dBz_dz = np.zeros (1247)
dBx_dx = np.zeros (1247)
Divergence = np.zeros (1247)
J = np.zeros (1247)

for m in range(1247):
    dBz_AE [m] = B_Z_THA [m]  - B_Z_THE_interp [m] 
    dBx_AE [m]  = B_X_THA [m]  - B_X_THE_interp [m] 

    dBz_DE [m]  = B_Z_THD_interp[m]  - B_Z_THE_interp [m] 
    dBx_DE [m]  = B_X_THD_interp [m]  - B_X_THE_interp [m] 

    dz_AE [m]  = state_Z_THA_interp [m]  - state_Z_THE_interp [m] 
    dx_AE [m]  = state_X_THA_interp [m]  - state_X_THE_interp [m] 

    dz_DE [m]  = state_Z_THD_interp [m]  - state_Z_THE_interp [m] 
    dx_DE [m]  = state_X_THD_interp [m]  - state_X_THE_interp [m] 

    dBz_dx [m]  = ((dBz_DE[m] *dz_AE [m] ) - (dBz_AE [m]  *dz_DE[m] ))/(dx_DE[m] *dz_AE[m]  - dx_AE[m] *dz_DE[m] );
    dBx_dz [m]  = ((dBx_AE [m] *dx_DE[m] ) - (dBx_DE [m] * dx_AE [m] ))/(dx_DE[m] *dz_AE[m]  - dx_AE[m] *dz_DE[m] );


    dBz_dz [m]  = (dBz_AE [m]  - (dBz_dx[m] *dx_AE [m] ))/(dz_AE [m] );
    dBx_dx [m]  = (dBx_AE [m]  - (dBx_dz[m] *dz_AE [m] ))/(dx_AE [m] );
    
    Divergence [m]  = ((dBx_dx[m]  - dBz_dz[m] )*1000)/1.3

    J [m]  = ((dBx_dz [m]  -  dBz_dx [m] )*1000)/1.3

#Blobe and length 
#Presettling the arrays
ion_avg_temp_THA = np.zeros (1247)
ion_avg_temp_THD = np.zeros (1247)
ion_avg_temp_THE = np.zeros (1247)
electron_avg_temp_THA = np.zeros (1247)
electron_avg_temp_THD = np.zeros (1247)
electron_avg_temp_THE = np.zeros (1247)
B_lobe_THA = np.zeros (1247)
B_lobe_THD = np.zeros (1247)
B_lobe_THE = np.zeros (1247)
B_lobe_avg  = np.zeros (1247)
Length = np.zeros (1247)
Temp_THA = np.zeros (1247)
Temp_THD = np.zeros (1247)
Temp_THE = np.zeros (1247)

for m in range (1247):
    
    
    ion_avg_temp_THA [m] = (ion_tperp1_THA_interp[m] + ion_tperp2_THA_interp[m] + ion_tpar_THA_interp[m])/3
    ion_avg_temp_THD [m] = (ion_tperp1_THD_interp[m] + ion_tperp2_THD_interp[m] + ion_tpar_THD_interp[m])/3
    ion_avg_temp_THE [m] = (ion_tperp1_THE_interp[m] + ion_tperp2_THE_interp[m] + ion_tpar_THE_interp[m])/3;

    electron_avg_temp_THA [m] = (electron_tperp1_THA_interp[m] + electron_tperp2_THA_interp[m] + electron_tpar_THA_interp[m])/3
    electron_avg_temp_THD [m] = (electron_tperp1_THD_interp[m] + electron_tperp2_THD_interp[m] + electron_tpar_THD_interp[m])/3
    electron_avg_temp_THE [m] = (electron_tperp1_THE_interp[m] + electron_tperp2_THE_interp[m] + electron_tpar_THE_interp[m])/3
    
    Temp_THA [m] = ion_avg_temp_THA [m] + electron_avg_temp_THA [m]
    Temp_THD [m] = ion_avg_temp_THD [m] + electron_avg_temp_THD [m]
    Temp_THE [m] = ion_avg_temp_THE [m] + electron_avg_temp_THE [m]

    B_lobe_THA [m] = math.sqrt(((B_X_THA [m])**2) + (B_Y_THA [m]**2) + (0.4*density_THA_interp[m]*Temp_THA[m]))
    B_lobe_THD [m] = math.sqrt(((B_X_THD_interp [m])**2) + (B_Y_THD_interp [m]**2) + (0.4*density_THD_interp[m]*Temp_THD[m]))
    B_lobe_THE [m] = math.sqrt(((B_X_THE_interp [m])**2) + (B_Y_THE_interp [m]**2) + (0.4*density_THE_interp[m]*Temp_THE[m]))
    
    
    B_lobe_avg [m] = (B_lobe_THA[m] + B_lobe_THE[m] + B_lobe_THD [m])/3

    Length [m] = abs((B_lobe_avg [m])/(1.3*(J[m])))


#Plotting Data
B_TIME_THA_conv = [datetime.utcfromtimestamp(x) for x in B_time_THA]



plt.plot(B_TIME_THA_conv, B_X_THA, 'b', B_TIME_THA_conv, B_X_THD_interp, 'k', B_TIME_THA_conv, B_X_THE_interp, 'r')
plt.title('Magnetic field Bx (THA, THD, THE satellites measurements)')
plt.xlabel('Time')
plt.ylabel('$Bx (nT)$')
plt.legend(["THA", "THD", "THE"], loc ="lower right")
plt.show()


plt.plot(B_TIME_THA_conv, B_Y_THA, 'b', B_TIME_THA_conv, B_Y_THD_interp, 'k', B_TIME_THA_conv, B_Y_THE_interp, 'r')
plt.title('Magnetic field By (THA, THD, THE satellites measurements)')
plt.xlabel('Time')
plt.ylabel('$By (nT)$')
plt.legend(["THA", "THD", "THE"], loc ="lower right")
plt.show()


plt.plot(B_TIME_THA_conv, B_Z_THA, 'b', B_TIME_THA_conv, B_Z_THD_interp, 'k', B_TIME_THA_conv, B_Z_THE_interp, 'r')
plt.title('Magnetic field Bz (THA, THD, THE satellites measurements)')
plt.xlabel('Time')
plt.ylabel('$Bz (nT)$')
plt.legend(["THA", "THD", "THE"], loc ="lower right")
plt.show()

plt.plot(B_TIME_THA_conv, ion_avg_temp_THA, 'b', B_TIME_THA_conv, ion_avg_temp_THD, 'k', B_TIME_THA_conv, ion_avg_temp_THE, 'r')
plt.title('Ion temperature (THA, THD, THE satellites measurements)')
plt.xlabel('Time')
plt.ylabel('$T_i$')
plt.legend(["THA", "THD", "THE"], loc ="lower right")
plt.show()

plt.plot(B_TIME_THA_conv, electron_avg_temp_THA, 'b', B_TIME_THA_conv, electron_avg_temp_THD, 'k', B_TIME_THA_conv, electron_avg_temp_THE, 'r')
plt.title('Electron temperature (THA, THD, THE satellites measurements)')
plt.xlabel('Time')
plt.ylabel('$T_e$')
plt.legend(["THA", "THD", "THE"], loc ="lower right")
plt.show()

plt.plot(B_TIME_THA_conv, velocity_X_THA_interp, 'g')
plt.xlabel('Time')
plt.ylabel('$V_x (km/s)$')
plt.title('Velocity THA x-axis')
plt.show()

plt.plot(B_TIME_THA_conv, Divergence)
plt.xlabel('Time')
plt.ylabel('$Divergence (nT/km)$')
plt.title('Divergence')
plt.show()


plt.plot(B_TIME_THA_conv, J)
plt.xlabel('Time')
plt.ylabel('$J (nA/m^2)$')
plt.title('Current Density')
plt.show()


plt.plot(B_TIME_THA_conv, B_lobe_THA, B_TIME_THA_conv, B_lobe_THD, B_TIME_THA_conv, B_lobe_THE, B_TIME_THA_conv, B_lobe_avg)
plt.title('Blobe')
plt.xlabel('Time')
plt.ylabel('$Blobe (nT)$')
plt.legend(["THA", "THD", "THE", "Average"], loc ="lower right")
plt.show()

plt.plot(B_TIME_THA_conv, Length)
plt.title('Current sheet thinning')
plt.xlabel('Time')
plt.ylabel('$L (x10^3 km)$')
plt.show()






