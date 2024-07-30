# utilizing slice and images into python
# Fruit Ninja Academy
# 06/16/22
# Dipakshi Pal

from fnmatch import translate
import numpy as np

fruits = np.array([["Apple","Banana","Blueberry","Cherry"],
["Coconut","Grapefruit","Kumquat","Mango"],
["Nectarine","Orange","Tangerine","Pomegranate"],
["Lemon","Raspberry","Strawberry","Tomato"]])

# PART A
# Extract the bottom right element in one command.

print(fruits[3,3])

# PART B
# Extract the inner 2x2 square in one command.

print(fruits[1:3:1,1:3:1])

# PART C
# Extract the first and third rows in one command.

print(fruits[0], fruits[2])

# PART D
# Extract the inner 2x2 square flipped vertically and horizontally in one command.

print(fruits[2][1:3][::-1], fruits[1][1:3][::-1])

# PART E
# Swap the first and last columns in three commands. Hint: make a copy of an array using the copy() method

fruits_new = np.copy(fruits)
fruits_new[:,0] = fruits_new[:,3]
fruits_new[:,3] = fruits[:,0]
print(fruits_new)

# PART F
# Replace every element with the string "SLICED!" in one command.

fruits[::] = "Sliced!"
print(fruits)