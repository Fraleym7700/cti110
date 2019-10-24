# Create a for loops that display image in book
# CTI-110 P4HW3 - Nested Loops
# Michael Fraley
# 10/9/19
#pseudocode
#Set number of steps
#create nested for loop to create the ## image in book
#have range and columns
NUM_STEPS = 6
for r in range(NUM_STEPS):
    print("#", end='')
    for c in range(r):
        print(' ', end='')
    print('#')
