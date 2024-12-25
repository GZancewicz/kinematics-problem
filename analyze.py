import math
import json

# Define the lengths of the arm segments
L1 = 4  # Length from base to elbow in inches
L2 = 7  # Length from elbow to end effector in inches

# Define the base position
base_position = (0, 12)  # Base is 12 inches above the ground

# Define the servo constraints
theta1_constraints = (0, 180)  # Theta1 is limited to [0°, 180°]
theta2_constraints = (0, 180)  # Theta2 is limited to [0°, 180°]

# Function to calculate the position of the elbow and end effector
def calculate_positions(theta1, theta2):
    # Calculate the position of the elbow
    elbow_x = base_position[0] + L1 * math.cos(math.radians(theta1))
    elbow_y = base_position[1] + L1 * math.sin(math.radians(theta1))
    elbow_position = (elbow_x, elbow_y)

    # Calculate the position of the end effector
    end_effector_x = elbow_x + L2 * math.cos(math.radians(theta1 + theta2))
    end_effector_y = elbow_y + L2 * math.sin(math.radians(theta1 + theta2))
    end_effector_position = (end_effector_x, end_effector_y)

    return elbow_position, end_effector_position

# Generate the working space
working_space = []

for theta1 in range(theta1_constraints[0], theta1_constraints[1] + 1):
    for theta2 in range(theta2_constraints[0], theta2_constraints[1] + 1):
        _, end_effector_pos = calculate_positions(theta1, theta2)
        working_space.append({
            "theta1": theta1,
            "theta2": theta2,
            "x": end_effector_pos[0],
            "y": end_effector_pos[1]
        })

# Write the working space to a JSON file
with open('working_space.json', 'w') as json_file:
    json.dump(working_space, json_file, indent=4)

print("Working space data has been written to working_space.json")
