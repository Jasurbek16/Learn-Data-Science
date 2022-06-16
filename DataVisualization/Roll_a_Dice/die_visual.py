import pygal
from die import Die
###############################################################
# rolling two six-sided dice
###############################################################
# # Create two D6s.
# die_1 = Die()
# die_2 = Die()
# # Make some rolls, and store results in a list
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# # Analyze the results
# frequencies = []
# max_result = die_1.side_num + die_2.side_num
# for value in range(2, max_result+ 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # Visualize the results.
# hist = pygal.Bar()

# hist.title = "Results of rolling two D6 dice 1000 times"
# hist.x_labels = [num for num in range(2, (die_1.side_num + die_2.side_num) + 1))]
# hist.x_title = "Result"
# hist._y_title = "The frequency of the result"

# hist.add('D6 + D6', frequencies)
# # ^ a series of values to the chart
# # ^ passing it a label for the set of values to be
# # added and a list of the values to appear on the chart
# hist.render_to_file('dice_visual.svg')

###############################################################
# rolling one six-sided and ten-sided dice
###############################################################
# # Create a D6 and a D10.
# die_1 = Die()
# die_2 = Die(10)
# # Make some rolls, and store results in a list
# results = []
# for roll_num in range(50000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# # Analyze the results
# frequencies = []
# max_result = die_1.side_num + die_2.side_num
# for value in range(2, max_result+ 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # Visualize the results.
# hist = pygal.Bar()

# hist.title = "Results of rolling a D6 and a D10 50000 times"
# hist.x_labels = [num for num in range(2, (die_1.side_num + die_2.side_num) + 1)]
# hist.x_title = "Result"
# hist._y_title = "The frequency of the result"

# hist.add('D6 + D10', frequencies)
# # ^ a series of values to the chart
# # ^ passing it a label for the set of values to be
# # added and a list of the values to appear on the chart
# hist.render_to_file('D10+D6_visual.svg')

###############################################################