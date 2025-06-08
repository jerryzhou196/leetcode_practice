import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from IPython.display import Image, display

from typing import *

from copy import copy


class Solution:
    def candy(self, ratings: List[int]) -> int:
        hasChanged = True
        n = len(ratings)
        count = [1] * n
        iterations = []

        # ratings = [1, 2, 1, 1, 1, 2, 3, 4]
        iteration_count = 0
        print(f"ratings:      {ratings}")

        while hasChanged:
            hasChanged = False
            print(f"iteration #{iteration_count}: {count}")
            for i in range(n):
                if (
                    i != n - 1
                    and ratings[i] > ratings[i + 1]
                    and count[i] <= count[i + 1]
                ):
                    count[i] += 1
                    hasChanged = True

                if i != 0 and ratings[i] > ratings[i - 1] and count[i] <= count[i - 1]:
                    count[i] += 1
                    hasChanged = True

                iterations.append(copy(count))

            iteration_count += 1

        return iterations


s = Solution()
ratings = np.random.randint(3, 8, 20)
iterations = s.candy(ratings)

x = np.arange(len(ratings))

# Create the figure and plot baseline (ratings)
fig, ax = plt.subplots()
ax.set_xlabel("Index")
ax.set_ylabel("Value")
ax.set_title("Ratings vs. Iterations")

# Baseline bars (ratings)
ax.bar(x, ratings, width=0.8, label="Ratings")

# Overlay bars for iterations (starting with iteration 0)
iter_bars = ax.bar(x, iterations[0], width=0.4, label="Iteration 0")

# Animation update function
def update(frame):
    current_iter = iterations[frame]
    for bar, height in zip(iter_bars, current_iter):
        bar.set_height(height)
    ax.set_title(f"Ratings vs. Iteration {frame}")
    return iter_bars


# Create the animation
anim = FuncAnimation(fig, update, frames=len(iterations), interval=10000, blit=False)

# Save and display the animation as GIF
anim.save("./bar_animation.gif", writer="pillow", fps=1)
plt.close(fig)  # Close the figure to avoid duplicate static output

# Display the saved GIF
display(Image("./bar_animation.gif"))
