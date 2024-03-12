import pandas as pd
import numpy as np
import datetime as dt
from pandas_datareader import data as pdr
from scipy.stats import norm, t
import matplotlib.pyplot as plt


a = np.array([1,2,3])
b = np.array([0,1,0])
a*b
np.inner(a,b)

mc_sims = 400
T = 100
meanM = np.full(shape = (T, 3), fill_value = 0.0)

portfolio_sims = np.full(shape = (T, mc_sims), fill_value = 0)










