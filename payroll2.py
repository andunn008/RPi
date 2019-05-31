# -*- coding: utf-8 -*-
"""
Created on Thu May 30 02:45:51 2019

@author: Andrew Dunn
"""

hours = float(input("Please enter the number of hours: "))
rate = float(input("Please enter the rate per hour: "))

def payroll(hours, rate):
    ORPH = rate * 1.5
    OverT = hours - 40
    if OverT > 0:
        OverP = OverT * ORPH
        NormP = 40 * rate
        TotalP = NormP + OverP
    else:
        TotalP = hours * rate
    print("Your Gross Pay is: %.2f" %TotalP)

payroll(hours, rate)
  
