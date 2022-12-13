import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

# Simulate rolling dice
def roll_dice(num_dices, size):
    rng = np.random.default_rng()

    # Roll the dice
    faces = rng.integers(low = 1, high = 6, endpoint = True, size = (size, num_dices))

    # Sum face values
    return np.sum(faces, axis = 1)

# Create empty zero-sized numpy array
face_counts = np.array([], dtype = int)

for i in range(0, 100):
    # Roll 1 dice
    dice_faces = roll_dice(2, 100)

    # Concatenate the new result to the previous results
    face_counts = np.concatenate((face_counts, dice_faces), axis = 0)

    # Plot histogram of all results
    hist = plt.hist(face_counts, bins = np.arange(1, 15) - 0.5, color = 'blue', rwidth = 0.8)

    # Set title and axis labels
    plt.title('Roll Dice')
    plt.xlabel('Dice Face')
    plt.ylabel('Count (Frequency)')

    plt.pause(0.1)

plt.show()