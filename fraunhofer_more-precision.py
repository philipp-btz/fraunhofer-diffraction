#
#   BTZ
#   base Unit m (Meters)

import numpy as np
import math as m
import matplotlib.pyplot as plt
import datetime
import gmpy2 as gm


p = 20         #   number of elemental wave samples taken from slit
q = 0.01       #   step size on projection Plane [m]
r = 30          #   calculation border. max allowed distance [m] off center
t = 60           #   amount of samples in time for intensity on plane



a = 16           #   distance [m] slit <--> projection plane
b = 1        #   width [m] of slit 
d = 0           #   distance off center projection plane
l = 0.05           #   wavelenghth of wave | in m
c = 3000  #   Speed of wave in m/s

class Fresnel:
    def __init__(self, p =8, q=0.1, r=2, t=8, a=1, b=0.1, l=5, c=300):
        self.num_samplewaves = p
        self.stepsize_projectionplane = q
        self.calculation_border = r
        self.timestops = t
        self.distance_slit_projectionplane = a
        self.width_slit = b
        self.wavelenghth = l
        self.speed = c
        self.period_duration = l / c
        pass

    def __str__(self):
        s =  "num_samplewaves "  + str(self.num_samplewaves) + "---stepsize_projectionplane " + str(self.stepsize_projectionplane) + "---calculation_border " + str(self.calculation_border) + "---timestops " + str(self.timestops) + "---distance_slit_projectionplane " + str(self.distance_slit_projectionplane) + "---width_slit " + str(self.width_slit) + "---wavelenghth " + str(self.wavelenghth) 
        t = s.split(".")
        u = "-".join(t)
        print(u)
        return u

    def distance(self, d=0):                      #   distance of sample points on slit to point on projection plane with distance d off center
        self.len_samplewaves = []
        for i in range(1, self.num_samplewaves + 1):
            gang = np.sqrt(self.distance_slit_projectionplane ** 2 + (d - 0.5*self.width_slit + i*(self.width_slit/self.num_samplewaves))**2)
            self.len_samplewaves.append(gang)
        return self.len_samplewaves
    
    def intensity_at_point(self):
        min_t = self.len_samplewaves[len(self.len_samplewaves)-1] / self.speed
        list_int_values = []
        sublist_int_values = []
        for t in range(0, self.timestops+1):
            for x in range(len(self.len_samplewaves)):
                intensity = np.sin((2*np.pi*(min_t+t))/self.period_duration - (2*np.pi*x)/self.wavelenghth)
                sublist_int_values.append(intensity)
            list_int_values.append(sum(sublist_int_values))
        intensity_at_point = max(list_int_values)
        return intensity_at_point

    def screen(self):
        self.plotlib = {}
        for d in range(0, m.ceil(self.calculation_border/self.stepsize_projectionplane)):
            self.distance(d)
            intensity_at_d = self.intensity_at_point()
            self.plotlib.update({d*self.stepsize_projectionplane : intensity_at_d})
        return self.plotlib
    
    def plot(self):
        x = self.plotlib.keys()
        y = self.plotlib.values()

        date = datetime.datetime.now()

        f_date = date.strftime("%Y-%m-%d %H:%M:%S")
        date = f_date.split(":")
        date = "-".join(date) 
        date = "Fresnel-Plot at " + date + "-- with ---" + str(self)
        plt.plot(x,y,"o")
        plt.savefig(date )
        plt.show()






p = Fresnel(p, q, r, t, a, b, l, c)
print(p.screen())
p.plot()