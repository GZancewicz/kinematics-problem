import json
import matplotlib.pyplot as plt
import os

def plot_working_space(json_file, output_file='working_space_plot.jpeg'):
    # Load the JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Assume data is a list of positions
    positions = data  # Directly use the list
    
    # Separate the positions into x and y coordinates
    x_coords = [pos['x'] for pos in positions]
    y_coords = [pos['y'] for pos in positions]
    
    # Create a scatter plot
    plt.figure(figsize=(8, 8))
    plt.scatter(x_coords, y_coords, c='gray', alpha=0.5, label='End Effector Positions')
    
    # Add horizontal lines at y=12 and y=1
    plt.axhline(y=12, color='black', linewidth=2, linestyle='--', label='y=12')
    plt.axhline(y=1, color='black', linewidth=2, linestyle='--', label='y=1')
    
    # Add labels and title
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Robot Arm Working Space')
    plt.legend()
    
    # Show the plot
    plt.grid(True)
    plt.axis('equal')  # Ensure the aspect ratio is equal
    
    # Save the plot to a JPEG file
    print(f"Saving plot to {output_file} in directory {os.getcwd()}")
    plt.savefig(output_file, format='jpeg')
    
    # Display the plot
    plt.show()

# Example usage
plot_working_space('working_space.json')
