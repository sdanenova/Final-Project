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


#FFT for B field
Fsb=16 # MMS B field sampling rate, for THEMIS
NFFT = 16*8 # 8 s window
wlen=NFFT #hanning window length
hp=NFFT*0.5 #4s overlapping
K = sum(np.hanning(wlen))/wlen #hanning weighting power

def stfto(x, wlen, h, nfft, fs):
#function: [stft, f, t] = stft(x, wlen, h, nfft, fs)
# x - signal in the time domain
# wlen - length of the hamming window
# h - hop size
# nfft - number of FFT points
# fs - sampling frequency, Hz
# f - frequency vector, Hz
# t - time vector, s
# stft - STFT matrix (only unique points, time across columns, freq across rows)

    xlen = len(x) #length of the signal
    win = np.hanning(wlen) #form a periodic hamming window
    
    #form the stft matrix
    rown = math.ceil((1+nfft)/2)    #calculate the total number of rows       
    coln = 1+np.fix((xlen-wlen)/h)  #calculate the total number of columns    
    stft = np.zeros(rown, coln)     #form the stft matrix
    
    #initialize the indexes
    indx = 0
    col = 0

    #perform STFT
    while indx + wlen <= xlen:
        #windowing
        xw = np.multiply(x[(indx):(indx+wlen)],win)
    
        # FFT
        X = fft(xw, nfft)
        #update the stft matrix
        stft[:, col] = X[0:rown]
        #update the indexes
        indx = indx + h
        col = col + 1
    
    #calculating the time and frequency vectors
    t = np.linspace((wlen/(2*fs)), ((wlen/2+(coln-1)*h)/fs), num = h)
    f = np.linspace(0,((rown-1)*fs/nfft))
    return (stft,f,t)

stftB,fB,tB=stfto(Bdata_THA[:,0],wlen,hp,NFFT,Fsb) 
 


        

