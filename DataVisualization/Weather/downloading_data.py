import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Extracting and Reading Data
# Get dates, high, and low temperatures from file.
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    dates, high_temps, lows = [], [], []
    for row in reader:
        try:   
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            high_temps.append(high)
            lows.append(low)

# Plotting Data in a Temperature Chart
# Plot data
fig = plt.figure(dpi=141, figsize=(10, 6))
plt.plot(dates, high_temps, color='red', alpha = 0.5)
# alpha -> controls the color's transparency; 1-opaque 0-transparent (completely)
plt.plot(dates, lows, c='blue', alpha = 0.5)
plt.fill_between(dates, high_temps, lows, facecolor = 'blue', alpha = 0.1)
# facecolor - the color of the shaded region

#Format plot
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize = 24)
fig.autofmt_xdate()
# ^ draws the date labels diagonally to prevent them from overlapping
plt.ylabel('Temperature (℉)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize=16)

plt.show()