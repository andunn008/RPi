# -*- coding: utf-8 -*-
"""
Created on Fri May 31 03:39:38 2019

@author: Andrew Dunn
"""

from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y = 2.0*sin(2*pi*t)

import copy
y_sat = copy.copy(y)

figure(1)
clf()
plot(t,y,'r--')

inds = where(y < 0.5)[0]
y_sat[inds] = 0.5

plot(t, y_sat, label = '$y(t)$', linewidth = 2.0)
ylable('$y(t)$')
xlable('Time (sec.)')
legend(loc = 1)

show()