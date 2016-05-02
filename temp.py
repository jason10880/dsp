
"""
###  4-1
f= open("123.csv")
s= f.read()
sL= s.split('\n')
xL= [x.split(',')[-1] for x in sL]
yL= [float(x) for x in xL[1:-4]]
priceData= np.array(yL)

print(len(priceData))
"""

"""  4-2
import pylab as pl
def movingaverage(x,length):
    y = np.convolve(x, np.ones(length)/length)
    y = y[:len(x)]
    return y
    
ma100 = movingaverage(priceData,100)
ma500 = movingaverage(priceData,500)
ma1000= movingaverage(priceData,1000)

pl.plot(priceData)
pl.plot(ma100)
pl.plot(ma500)
pl.plot(ma1000)
"""

"""  4-3
print(priceData[1000:1005])
print(ma100[1000:1005])
print(ma500[1000:1005])
print(ma1000[1000:1005])
"""

""" 4-4
import pandas as pd
import numpy as np
import thinkdsp
import thinkplot
df = pd.read_csv('123.csv',nrows=2112,parse_dates=[0])
ys = df.Close.values
ts = np.arange(len(ys))
wave = thinkdsp.Wave(ys,ts,framerate=1)
wave.plot()
thinkplot.config(xlabel='Time(days)')

spectrum = wave.make_spectrum()
spectrum.plot_power()
thinkplot.config(xlabel='Frequency (1/days)',
                 xscale='log', yscale='log')
"""

"""  4-5 & 4-6
import pandas as pd
import numpy as np
import thinkdsp
import thinkplot
df = pd.read_csv('123.csv',nrows=2112,parse_dates=[0])
ys = df.Close.values
ts = np.arange(len(ys))

duration=len(ys)
framerate = 20
linewidth = 1

signal1 = thinkdsp.UncorrelatedUniformNoise()
wNoise = signal1.make_wave(duration=duration,framerate=framerate)
wNoise.plot()


signal2 = thinkdsp.PinkNoise()
pNoise = signal2.make_wave(duration=duration,framerate=framerate)
pNoise.plot()

signal3 = thinkdsp.BrownianNoise()
rNoise = signal3.make_wave(duration=duration,framerate=framerate)
rNoise.plot()
"""

""" 4-7
def make_spectrum(signal):
        wave = signal.make_wave(duration=duration, framerate=framerate)
        spectrum = wave.make_spectrum()
        spectrum.hs[0] = 0
        return spectrum

signal1 = thinkdsp.UncorrelatedUniformNoise()
white = make_spectrum(signal1)
white.plot_power(label='white',color='#000000',linewidth=linewidth)

signal2 = thinkdsp.PinkNoise()
pink = make_spectrum(signal2)
pink.plot_power(label='pink', color='#FFC0CB', linewidth=linewidth)

signal3 = thinkdsp.BrownianNoise()
red = make_spectrum(signal3)
red.plot_power(label='red', color='#FF0000', linewidth=linewidth)

thinkplot.config(xlabel='frequency (Hz)',
                 ylabel='power',
                 xscale='log',
                 yscale='log')
"""
