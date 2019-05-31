# -*- coding: utf-8 -*-
"""
Created on Thu May 30 02:45:51 2019

@author: Andrew Dunn
"""

Hours = int(input("Please enter the number of hours: "))
RPH = int(input("Please enter the rate per hour: "))

ORPH = RPH * 1.5
OverT = Hours - 40

if OverT > 0:
    OverP = OverT * ORPH
    NormP = 40 * RPH
    TotalP = NormP + OverP
    print(TotalP)
else:
    NormP = Hours * RPH
    print(NormP)