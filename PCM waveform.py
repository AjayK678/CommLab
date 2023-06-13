# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:46:03 2023

@author: Student
"""

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0,0.05,0.0005) #Defining the time interval
fm = 100 #Assume the frequency of message signal to be 100 Hz
a = 1 #Let the amplitude of the signal be 1v
x_t= np.sin(2*np.pi*fm*t)#x(t) is generated
fig, axs = plt.subplots(2,2,layout="tight")
plt.suptitle("Performance of Waveform Coding Using PCM")
axs[0,0].plot(t,x_t)
axs[0,0].set_title("Message Signal")
axs[0,0].grid(axis = 'y')
axs[0,0].set_xlabel('t->')
axs[0,0].set_ylabel('x(t) ->')
""" DC offset so that it takes only positive amplitude value can be created by adding 1 to x(t) """
x_t_o = x_t + 1
axs[0,1].plot(t,x_t_o,'tab:red')
axs[0,1].set_title("Message Signal with postive values only")
axs[0,1].grid(axis = 'y')
axs[0,1].set_xlabel('t->')
axs[0,1].set_ylabel('x(t)+1 ->')
fs = 10*fm #sampling frequency 2 times fm
Ts = 1/fs #sampling time
n = np.random.randint(2, size=len(t))
nT = n*Ts
T = np.arange(0,0.05,Ts)
x_s = np.sin(2*np.pi*fm*T)
axs[1,0].stem(T,x_s)
axs[1,0].set_title("Sampled signal x(nTs)")
axs[1,0].grid(axis = 'y')
axs[1,0].set_xlabel('t->')
axs[1,0].set_ylabel('x(nTs) ->')
"quantize the signal using an uniform quantizer"
n = 3 # Number of bits for encoding
L = 2**n # Number of quantization levels
x_max = round(max(x_t))
x_min = round(min(x_t))
delta = (x_max-x_min)/2
print("Step Size =", delta)
Q_levels = np.linspace(x_min,x_max,L+1)
x_q_1 = [] #quantized signal
for i in x_s:
    for j in Q_levels:
        if i<= j:
             x_q_1.append(j)
             break
x_q = np.linspace(0,2*x_max,L,endpoint = False)
t_axis = t[0:len(x_q)]
axs[1,1].step(t_axis,x_q,'tab:green')
axs[1,1].set_title("Quantized signal")
axs[1,1].grid(axis = 'y')
axs[1,1].grid(axis = 'x')
axs[1,1].set_xlabel('t->')
axs[1,1].set_ylabel('Quantized signal ->')
" Binary encoding of quantized signal"
"Quantization noise"
e_q = x_q_1-x_s
print(f"The observed quantization noise for n= {n}", e_q)
"Signal to noise ratio in dB"
n = [5,6,7,8,9]
gamma=[]
for i in range(len(n)):
    gamma.append(1.8+6*n[i])
fig1, ax = plt.subplots(1,1)
ax.plot(n,gamma)
ax.set_title("SNR vs Number of bits per symbol")
ax.grid(axis = 'y')
ax.set_xlabel('Number of bits per symbol')
ax.set_ylabel('SNR')
