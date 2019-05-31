# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:27:37 2019

@author: Andrew Dunn
"""

from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y = 2.0*sin(2*pi*t)

N = len(y)
y_sat = zeros(N)

for i in range(N):
    y_i = y[i]
    if y_i < 0.5:
        y_sat[i] = 0.5
    else:
        y_sat[i] = y_i

figure(1)
clf()
plot(t,y,'r--')
plot(t, y_sat, label = '$y(t)$', linewidth = 2.0)
ylable('$y(t)$')
xlable('Time (sec.)')
legend(loc = 1)

show()