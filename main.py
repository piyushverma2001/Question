import time

def rabbit_direction(x):
    # Observing at t=0
    initial_postition = rabbit_present(x)
    
    # Waiting for 1 second
    time.sleep(1)
    
    # Observing at t=1
    final_position = rabbit_present(x)
    
    # Determine direction based on observations
    if final_position == initial_postition:
        return 0  # Rabbit did not move (Not possible)
    elif final_position:
        return 1  # Rabbit moved in positive direction
    else:
        return -1  # Rabbit moved in negative direction

# Function to check if rabbit is present at position x at the current time
def rabbit_present(x):
    # Function to check if rabbit is at position x at the current time, this function can return True or False randomly or based on some logic
    # For simplicity, assume it returns True if the rabbit is at position x, False otherwise
    return bool(random.choice([0, 1]))

import random

# Test with a random starting position
starting_position = random.randint(-100, 100)
direction = rabbit_direction(starting_position)

if direction == 1:
    print(f"The rabbit is moving in the positive direction from position {starting_position}.")
elif direction == -1:
    print(f"The rabbit is moving in the negative direction from position {starting_position}.")
else:
    print(f"The rabbit did not move from position {starting_position}.")
