## Filename: March2013PDS.py
## Author: Claire Hinrichs
## Description: This file creates Power Density Spectrum for the March 2013 Flare observed with LAT


import numpy as np
import matplotlib.pyplot as plt


# Import and define data variables from obrital light curve

data=np.genfromtxt('lc_figure2_orbits.lc.txt', skip_header=3).transpose()
times = data[0]
timee = data[1]   #Time Error
flux = data[2]
fluxe = data[3]   #Flux Error

# Defined a function used to create a scatter plot

def ScatterPlot():
    plt.errorbar(times,flux, xerr=timee, yerr=fluxe, fmt='.')
    plt.title('Crab Flare March 2013')
    plt.xlabel('Time (MJD)')
    plt.ylabel('Flux (10^{-6}s^{-1}cm^{-2})')
    plt.xticks(np.arange(56346,56372,2),fontsize = 8)
    plt.show()

ScatterPlot()  #Run the scatter plot function to plot the flux vs. time lught curve from LAT

# Interpolate observational data into equally time spaced bins to prepare for Fouier analysis

n = 2000       # number of desried points after interpolation
xintrp = np.arange(np.min(times),np.max(times),(np.max(times)-np.min(times))/n)      # time interpolation
yintrp = np.interp(xintrp,times,flux)      # flux interpolation using interpolated times
plt.plot(xintrp,yintrp)      # plot interpolated data
plt.show()


# Compute the one-dimensional discrete Fourier Transform for real input

ft = abs(np.fft.fft(yintrp))       # absolute value of the fourier transform
freq = abs(np.fft.fftfreq(len(yintrp), xintrp[0]-xintrp[1]))     # Discrete Fourier Transform sample frequencies

# Plot Power Desnity Spectrum in log-log space with noise floor indicated

plt.loglog(freq, ft)
plt.axhline(y=10, c='r', alpha = 0.2 , linewidth = 20)
plt.xlabel('Frequency (1/days)')
plt.ylabel('Power Density (flux^2/day)')
plt.title('Power Density Spectrum: March 2013 Flare')
plt.show()



