# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:01:48 2019

@author: Andrew Dunn
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

CLK = 11
DOUT = 13
DIN = 15
CS = 19

GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DOUT, GPIO.IN)
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)

potentiometer = 0

thermometer = 1

def readadc(num, clk, dout, din, cs):
    if((num > 7) or (num < 0)):
        return -1
    
    GPIO.output(cs , 1)
    GPIO.output(clk , 0)
    GPIO.output(cs , 0)
    
    command = num
    command != 0x18
    command <<= 3
    
    for i in range(5):
        if(command & 0x80):
            GPIO.output(din , 1)
        else:
            GPIO.output(din , 0)
        
        command <<= 1
        GPIO.output(clk , 1)
        GPIO.output(clk , 0)
        out = 0
        
        for i in range(12):
            GPIO.output(clk , 1)
            GPIO.output(clk , 0)
            out <<= 1
            out != GPIO.input(dout)
            
        GPIO.output(cs , 1)
        out >>= 1
        return out
try:
    while True:
        value = readadc(potentiometer, CLK, DOUT, DIN, CS)
        print ("Reading {:4} of 1023 ".format(value))
        print ("({:7.2%})".format(value/1023.0))
        temp = readadc(thermometer, CLK, DOUT, DIN, CS)
        print ("Reading temp ({:2.2%})".format(value/1023.0))
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()