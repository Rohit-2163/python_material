import matplotlib.pyplot as pl
import numpy as np
import math as m

#***********
x= [i for i in list(np.arange(0,20,0.05))]
y= [m.sin(i) for i in list(np.arange(0,20,0.05))]
pl.plot(x,y)
pl.xlabel("x-axis")
pl.ylabel("y-axis")
pl.title("Sine Curve")
pl.show()

#***************
x= [i for i in list(np.arange(0,15,0.05))]
y= [m.cos(i) for i in list(np.arange(0,15,0.05))]
pl.plot(x,y)
pl.xlabel("x-axis")
pl.ylabel("y-axis")
pl.title("Cosine Curve")
pl.show()

#***************
x= [i for i in list(np.arange(-1,1,0.05))]
y= [i**2 for i in list(np.arange(-1,1,0.05))]
pl.plot(x,y)
pl.xlabel("x-axis")
pl.ylabel("y-axis")
pl.title("y=x^2")
pl.show()

#***************
x= [i for i in list(np.arange(0,1,0.05))]
y= [m.exp(i) for i in list(np.arange(0,1,0.05))]
pl.plot(x,y)
pl.xlabel("x-axis")
pl.ylabel("y-axis")
pl.title("y=e^x")
pl.show()
