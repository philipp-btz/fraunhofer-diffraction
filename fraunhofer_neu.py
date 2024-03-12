#
#   BTZ
#   base Unit m (Meters)

import numpy as np
import math as m
import matplotlib.pyplot as plt
import time
import datetime


p = 8           #   number of elemental wave samples taken from slit
q = 0.05        #   step size on projection Plane [m]
r = -1          #   calculation border. max allowed distance [m] off center. no border is negative 



a = 6           #   distance [m] slit <--> projection plane
b = 0.01        #   width [m] of slit 
d = 0           #   distance off center projection plane
l = 1            #   wavelenghth of wave | in m


a = datetime.datetime.now()
print(time.localtime())
print(a)
#for i in range(len(a)):
 #   if a[1] == " ":

date = datetime.datetime.now()

f_date = date.strftime("%Y-%m-%d %H:%M:%S")
date = f_date.split(":")
date = "-".join(b)


#l = [1,2,3,4,5,6,7,8,9]
#print(len(l))
#print(l[len(l)])