#importing libraries
import os
import datetime
from datetime import datetime
import matplotlib.pyplot as plt
os.environ["CDF_LIB"] = "C:/Program Files/CDF_Distribution/cdf38_1-dist/lib"
from spacepy import pycdf
import numpy as np
import math
from scipy import signal
from scipy.fft import fft, ifft

#Reading Data

#Magnetic field
cdf = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/tha_l2_fgm_20160103_v01.cdf')
Bdata_THA = cdf['tha_fgl_gsm'][...]
Btime_THA = cdf['tha_fgl_time'][...]

#Electric field
cdf2 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/tha_l1_eff_20160103_v01.cdf')
Edata_THA = cdf2['tha_eff'][...]
Etime_THA = cdf2['tha_eff_time'][...]

#ion velocity 
cdf15 = pycdf.CDF('C:/Program Files/matlab_cdf381_patch/tha_l2_mom_20160103_v01.cdf')
VelIon_THA = cdf15['tha_peim_velocity_gsm'][...]
IonMOMTime_THA = cdf15['tha_peim_time'][...]
VelElect_THA = cdf15['tha_peem_velocity_gsm'][...]

#sampling rate parameters for magnetic field
fs=16 
NFFT = 16*8

#applying stft function on Bfield data to perform FFT
f, t, Zxx = signal.stft(Bdata_THA[:,0], fs, nperseg=NFFT)
#plotting colormap of the signal
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=0.01)
plt.title('STFT Magnitude Bx')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

#applying stft function on Bfield data to perform FFT
f1, t1, Zxx1 = signal.stft(Bdata_THA[:,1], fs, nperseg=NFFT)
#plotting colormap of the signal
plt.pcolormesh(t1, f1, np.abs(Zxx1), vmin=0, vmax=0.01)
plt.title('STFT Magnitude By')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

#applying stft function on Bfield data to perform FFT
f2, t2, Zxx2 = signal.stft(Bdata_THA[:,2], fs, nperseg=NFFT)
#plotting colormap of the signal
plt.pcolormesh(t2, f2, np.abs(Zxx2), vmin=0, vmax=0.01)
plt.title('STFT Magnitude Bz')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()


#Sampling rate parameters for Velocity

fv = 0.5
NFFT1 = 4*8
#applying stft function on velocity data to perform FFT
f3, t3, Zxx3 = signal.stft(VelIon_THA[:,0], fv, nperseg=NFFT)
#plotting colormap of the signal
plt.pcolormesh(t3, f3, np.abs(Zxx3), vmin=0, vmax=10)
plt.title('STFT Magnitude Vi')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
#applying stft function on velocity data to perform FFT
f4, t4, Zxx4 = signal.stft(VelElect_THA[:,0], fv, nperseg=NFFT)
#plotting colormap of the signal
plt.pcolormesh(t4, f4, np.abs(Zxx4), vmin=0, vmax=30)
plt.title('STFT Magnitude Ve')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

#Sampling rate parameters for Electric field
fE = 8
NFFT2 = 8*8
#applying stft function on Efield data to perform FFT
f5, t5, Zxx5 = signal.stft(Edata_THA[:,0], fE, nperseg=NFFT)
#plotting colormap of the signal
plt.pcolormesh(t5, f5, np.abs(Zxx5), vmin=0, vmax=10)
plt.title('STFT Magnitude Ex')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

#applying stft function on Efield data to perform FFT
f6, t6, Zxx6 = signal.stft(Edata_THA[:,1], fE, nperseg=NFFT)
#plotting colormap of the signal
plt.pcolormesh(t6, f6, np.abs(Zxx6), vmin=0, vmax=10)
plt.title('STFT Magnitude Ey')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

#applying stft function on Efield data to perform FFT
f7, t7, Zxx7 = signal.stft(Edata_THA[:,2], fE, nperseg=NFFT)
#plotting colormap of the signal
plt.pcolormesh(t7, f7, np.abs(Zxx7), vmin=0, vmax=1)
plt.title('STFT Magnitude Ez')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()