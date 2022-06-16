# import matplotlib.pyplot as plt
# -----------------------------------------------------------------
# basic
# -----------------------------------------------------------------

# input_vals = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_vals, squares, linewidth=5)
# # ^ linewidth parameter controls the thickness of the line
# # ^ it assumes the first data
# # int corresponds to an x-coordinate value of 0
# # Sol: giving plot() both the input and output values used to
# # calculate the squares

# # Set chart title and label axes
# plt.title("Squares", fontsize=22)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Squared result", fontsize=14)

# # Set size of tick labels
# plt.tick_params(axis='both', labelsize=14)
# # ^ styles the tick marks

# -----------------------------------------------------------------
# using the scatter() to graph a pt
# -----------------------------------------------------------------

# plt.scatter(4, 6, s=200)
# #                   ^ set the size of the dots used to draw the graph
# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# plt.tick_params(axis='both', which='major', labelsize=14)
# #                             ^ apply arguments to which ticks
# # there could be minor ticklabels as well but by def they are not present

# -----------------------------------------------------------------
# passing scatter() separate lists of x- and y-values
# -----------------------------------------------------------------
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)


# -----------------------------------------------------------------
# Calculating Data Automatically
# Removing Outlines from Data Points
# Defining Custom Colors
# -----------------------------------------------------------------

# x_vals = list(range(1, 1001))
# y_vals = [x**2 for x in x_vals]

# plt.scatter(x_vals, y_vals, c='red', edgecolor='none', s=10)
#                define a color ^     ^ remove the outlines around points
#       could be in an RGB mode ^ <- has to be between 1 and 0


# plt.scatter(x_vals, y_vals, c=y_vals,
#             cmap=plt.cm.Blues, edgecolor='none', s=40)
# ^ Using a Colormap
#             ^ are used in visualizations to emphasize a pattern in the data
# tell pyplot which colormap to use through the cmap argument
# ^ You can see all the colormaps available in pyplot at http://matplotlib.org/; go to
# Examples, scroll down to Color Examples, and click colormaps_reference.

# Set the range for each axis.
# plt.axis([0, 1100, 0, 1100000])

# plt.show()
# ^ opens matplotlib’s viewer and displays the plot
# use plt.savefig('filename_for_plot_img.png', bbox_inches='tight')
# The second argument trims extra whitespace from the plot ^
