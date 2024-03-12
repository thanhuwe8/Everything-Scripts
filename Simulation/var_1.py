import scipy.stats as stats
from scipy import sqrt, exp, pi
import scipy

import numpy as np


# Value at Risk: the maximum loss with a confidence level over a predetermied period

# Normal distribution
d1 = stats.norm.pdf(0, 0.1, 0.05) #estimate the density
d2 = 1/sqrt(2*pi*0.05**2)*exp(-(0-0.1)**2/0.05**2/2)

# standard normal distribution
d1 = stats.norm.pdf(0)
d1

x = scipy.arange(-3,3,0.1)
y = scipy.stats.norm.pdf(x)


# VaR = position*(mu - z * sigma_p)
z = scipy.stats.norm.ppf(1-0.99) # 1% chance that X < z

# 5% VaR of a hypothetical profit and loss probability density function
z = scipy.stats.norm.ppf(1 - 0.95)
f = lambda t: scipy.stats.norm.pdf(t)


# Expected Shortfall
x = np.arange(-3, 3, 0.1)
ret = scipy.stats.norm.pdf(x)
confidence = 0.975
position = 10000
z = stats.norm.ppf(1 - confidence)
zES = -stats.norm.pdf(z)/(1-confidence)
std = scipy.std(ret)
zES
ES = position*zES*std



# Historical VaR Calculation
import numpy as np
import enum







