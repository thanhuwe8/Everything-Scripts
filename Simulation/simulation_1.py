import random
import numpy as np

# Irwin-hall distribution
def randomNumber_1(n=12):
    a = []
    for i in range(0,n):
        a.append(random.random())
    rn = np.sqrt(12.0/float(n))*(np.sum(a)-n/2.0)
    return rn

# GBM analytical solution using Ito's lemma
def geometricBrownian(s_tminus1, mu, dt, vol):
    dW = randomNumber_1()*np.sqrt(dt)
    s_t = s_tminus1 * np.exp((mu-vol*vol/2.0)*dt + vol*dW)
    return(s_t)

# Vasicek
def vasicek(r_tminus1, vol, dt):
    a = 0.05
    b = 0.04
    dW = randomNumber_1()*np.sqrt(dt)
    d_r = a*(b - r_tminus1)*dt + vol*dW
    r_t = r_tminus1 + d_r
    return r_t

# HestonVol
def hestonVol(vol, dt):
    theta = 0.5
    w = 0.16
    etha = 0.2
    
    dB = randomNumber_1(n)*np.sqrt(dt)
    if 2*theta*w <= etha**2:
        raise Exception("Feller condition is breached for Heston Model")

    var_tminus1 = vol**2
    















