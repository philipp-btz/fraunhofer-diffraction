#
#   BTZ
#   base Unit m (Meters)

import numpy as np
import math as m
import matplotlib.pyplot as plt


p = 8           #   number of elemental wave samples taken from slit
q = 0.05        #   step size on projection Plane
r = -1          #   calculation border. max allowed distance off center. no border is negative



a = 6           #   distance slit <--> projection plane
b = 0.01        #   width of slit
d = 0           #   distance off center projection plane
l = 500         #   wavelenghth of light | in nm





def eff_int(l, d1, d2) :                    # Convolution of two sample waves
    p1 = np.arcsin(d1 / l * (10**-9))               # phase angle of sample 1
    p2 = np.arcsin(d2 / l * (10**-9))               # phase angle pf sample 2
    intensity = (np.sin(p1) + np.sin(p2) ) /2   # convolution of given waves
    return intensity


def smpl_point(d , a, b, p):
    raylib = []
    for i in range(1,p+1):
        gang = np.sqrt(a**2 + (d - 0.5 * b + i*(b/p) ))  #distance from samplepoint to given point on screen
        raylib.append(gang)
    return raylib

def int_at_point(raylib, l)
    for i in range(1, len(raylib)):
        eff_int(l, raylib[1], raylib[i])


        #hhfghfgh