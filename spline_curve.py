import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import KroghInterpolator
from enum import Enum, unique
import random 
from scipy.interpolate import PchipInterpolator

x= np.array([0, 1, 2, 3, 4, 5, 6, 7])
y= np.array([3, 4, 3.5, 2, 1, 1.5, 1.25, 0.9])

@unique
class Interp1dKind(Enum):
    LINEAR = 'linear'
    ZERO = 'zero'
    SLINEAR = 'slinear'
    QUADRATIC = 'quadratic'
    CUBIC = 'cubic'
    FIFTH_POWER = 5
    SEVENTH_POWER = 7

def AddNoise(input, disturbance_range=0.05):
    for i in range(0, x.shape[0]):
        input[i] += input[i] * random.uniform(-disturbance_range, disturbance_range)
    output = input
    return output
    

def GetInterp1dCurve(x, y, point_num=100, interp1_kind=Interp1dKind.FIFTH_POWER, disturbance_range=0.05):
    AddNoise(y, disturbance_range)
    g = KroghInterpolator(x,y)
    def f_(t):
        return np.log1p(g(t))
    xx = np.linspace(x.min(), x.max(), point_num)
    fig,ax = plt.subplots(figsize=(8,4))
    f = interp1d(x, f_(x), kind=interp1_kind.value)
    ax.plot(xx, f(xx), label=interp1_kind.value)
    ax.legend()
    ax.set_ylabel(r"$y$", fontsize=18)
    ax.set_xlabel(r"$x$", fontsize=18)
    plt.show()

def GetPchipInterpolatorCurve(x, y, point_num=100, disturbance_range=0.05):
    AddNoise(y, disturbance_range)
    g = KroghInterpolator(x,y)
    def f_(t):
        return np.log1p(g(t))
    xx = np.linspace(x.min(), x.max(), point_num)
    interpolant = PchipInterpolator(xx, f_(xx))
    fig,ax = plt.subplots(figsize=(8,4))
    ax.plot(xx, interpolant(xx))
    ax.legend()
    ax.set_ylabel(r"$y$", fontsize=18)
    ax.set_xlabel(r"$x$", fontsize=18)
    plt.show()
    

GetPchipInterpolatorCurve(x, y)

    