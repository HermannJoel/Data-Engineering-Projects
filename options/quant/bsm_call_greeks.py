#
# Black-Scholes-Merton (1973) European Call Option Greeks
# bsm_call_greeks.py
#
# credit to (c) Dr. Yves J. Hilpisch
# Derivatives Analytics with Python
#
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'
import mpl_toolkits.mplot3d.axes3d as p3
from bsm_option_valuation import d1f, N, dN

#
# Functions for Greeks
#
def BSM_delta(St, K, t, T, r, sigma):
    ''' Black-Scholes-Merton DELTA of European call option.
    Parameters
    ==========
    St: float
        stock/index level at time t
    K: float
        strike price
    t: float
        valuation date
    T: float
        date of maturity/time-to-maturity if t = 0; T > t
    r: float
        constant, risk-less short rate
    sigma: float
        volatility
    Returns
    =======
    delta: float
        European call option DELTA
    '''
    d1 = d1f(St, K, t, T, r, sigma)
    delta = N(d1)
    return delta

def BSM_gamma(St, K, t, T, r, sigma):
    ''' Black-Scholes-Merton GAMMA of European call option.
    Parameters
    ==========
    St: float
        stock/index level at time t
    K: float
        strike price
    t: float
        valuation date
    T: float
        date of maturity/time-to-maturity if t = 0; T > t
    r: float
        constant, risk-less short rate
    sigma: float
        volatility
    Returns
    =======
    gamma: float
        European call option GAMMA
    '''
    d1 = d1f(St, K, t, T, r, sigma)
    gamma = dN(d1) / (St * sigma * math.sqrt(T - t))
    return gamma

def BSM_theta(St, K, t, T, r, sigma):
    ''' Black-Scholes-Merton THETA of European call option.
    Parameters
    ==========
    St: float
        stock/index level at time t
    K: float
        strike price
    t: float
        valuation date
    T: float
        date of maturity/time-to-maturity if t = 0; T > t
    r: float
        constant, risk-less short rate
    sigma: float
        volatility
    Returns
    =======
    theta: float
        European call option THETA
    '''
    d1=d1f(St, K, t, T, r, sigma)
    d2=d1 - sigma * math.sqrt(T - t)
    theta= -(St * dN(d1) * sigma / (2 * math.sqrt(T - t)) + r * K * math.exp(-r * (T - t)) * N(d2))
    return theta

def BSM_rho(St, K, t, T, r, sigma):
    ''' Black-Scholes-Merton RHO of European call option.
    Parameters
    ==========
    St: float
        stock/index level at time t
    K: float
        strike price
    t: float
        valuation date
    T: float
        date of maturity/time-to-maturity if t = 0; T > t
    r: float
        constant, risk-less short rate
    sigma: float
        volatility
    Returns
    =======
    rho: float
    European call option RHO
    '''
    d1=d1f(St, K, t, T, r, sigma)
    d2=d1 - sigma * math.sqrt(T - t)
    rho=K * (T - t) * math.exp(-r * (T - t)) * N(d2)
    return rho

def BSM_vega(St, K, t, T, r, sigma):
    ''' Black-Scholes-Merton VEGA of European call option.
    Parameters
    ==========
    St: float
        stock/index level at time t
    K: float
        strike price
    t: float
        valuation date
    T: float
        date of maturity/time-to-maturity if t = 0; T > t
    r: float
        constant, risk-less short rate
    sigma: float
        volatility
    Returns
    =======
    vega: float
        European call option VEGA
    '''
    d1=d1f(St, K, t, T, r, sigma)
    vega=St * dN(d1) * math.sqrt(T - t)
    return vega
#
# Plotting the Greeks
#

def plot_greeks(function, greek):
    # Model Parameters
    St = 100.0 # index level
    K = 100.0 # option strike
    t = 0.0 # valuation date
    T = 1.0 # maturity date
    r = 0.05 # risk-less short rate
    sigma = 0.2 # volatility
    # Greek Calculations
    tlist = np.linspace(0.01, 1, 25)
    klist = np.linspace(80, 120, 25)
    V = np.zeros((len(tlist), len(klist)), dtype=np.float)
    for j in range(len(klist)):
        for i in range(len(tlist)): 
            V[i, j] = function(St, klist[j], t, tlist[i], r, sigma)
    # 3D Plotting
    x, y = np.meshgrid(klist, tlist)
    fig = plt.figure(figsize=(9, 5))
    plot = p3.Axes3D(fig)
    plot.plot_wireframe(x, y, V)
    plot.set_xlabel('strike $K$')
    plot.set_ylabel('maturity $T$')
    plot.set_zlabel('%s(K, T)' % greek)