import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []


index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    plt.cla()
    # ^ to clear out axis 
    plt.plot(x_vals, y_vals) 
    
ani = FuncAnimation(plt.gcf(), animate, interval=1000)#<- 1000 - 1secon d
# ^ args: 1st: current figure we want to animate
#         2nd: function for animation
#         3rd: interval of how often running

plt.tight_layout()
plt.show()

