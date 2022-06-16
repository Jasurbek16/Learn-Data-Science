# -----------------------------------------------------
# Random Walks
# -----------------------------------------------------
from random import choice
import matplotlib.pyplot as plt

# we’ll store possible choices in a list and
# use choice() to decide which choice to use
# each time a decision is made


class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_pts=5000):
        """Initialize attributes of a walk."""
        self.num_pts = num_pts

        # All walks start at (0, 0)
        self.x_vals = [0]
        self.y_vals = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until
        # the walk reaches the desired length
        while len(self.x_vals) < self.num_pts:
            # Decide which direction to go and
            # how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            # (The inclusion of a 0 allows us to take
            # steps along the y-axis as well as steps
            # that have movement along both axes.)
            x_step = x_direction * x_distance
            # ^ determine the length of
            # each step in the x direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # ^ # ^ determine the length of
            # each step in the y direction

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_vals[-1] + x_step
            next_y = self.y_vals[-1] + y_step

            self.x_vals.append(next_x)
            self.y_vals.append(next_y)


# Keep making new walks, as long as the program is active.
while True:

    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window
    plt.figure(dpi = 141 ,figsize=(10, 6))
    # ^ controls the width, height, resolution, and background color of the plot

    point_numbers = list(range(rw.num_pts))
    # plot according to the moves to see from where to where we went
    plt.scatter(rw.x_vals, rw.y_vals, c=point_numbers,
                cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and last points
    plt.scatter(0,0, c='green', edgecolors='none', s=100)
    # the starting ^  point
    plt.scatter(rw.x_vals[-1], rw.y_vals[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break