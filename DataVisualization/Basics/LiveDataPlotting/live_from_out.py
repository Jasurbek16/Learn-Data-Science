from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    # ^ to clear out axis 
    # ^ clears out our legend but we would recreate that below

    plt.plot(x, y1, label='Channel 1') 
    plt.plot(x, y2, label='Channel 2') 
    
    plt.legend(loc='upper left')
    # ^ recreating
    # ^ we are setting the loc coz that avoids switches around
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)#<- 1000 - 1secon d
# ^ args: 1st: current figure we want to animate
#         2nd: function for animation
#         3rd: interval of how often running

plt.tight_layout()
plt.show()


