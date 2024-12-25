# Robotic Arm Working Space Analysis

This project models and visualizes the working space of a two-segment robotic arm. The scripts calculate possible positions of the arm's end effector and provide visualizations of its reachability.

## Files and Descriptions

### `analyze.py`
- **Purpose**: Defines the parameters and constraints for a two-segment robotic arm. It calculates the positions of the elbow and end effector for all possible angles of the arm segments (`theta1` and `theta2`) within specified constraints.
- **Output**: Generates a JSON file (`working_space.json`) containing the angles and corresponding end effector positions.

### `plot_workspace.py`
- **Purpose**: Reads the `working_space.json` file and visualizes the working space of the robotic arm.
- **Functionality**: Likely uses a plotting library like `matplotlib` to create a graphical representation of all possible positions the end effector can reach.

### `plot_alt_workspace.py`
- **Purpose**: Provides an alternative visualization of the working space.
- **Functionality**: Uses different plotting techniques or parameters to offer another perspective on the arm's reachability.

### `create_alt_working_space.py`
- **Purpose**: Generates an alternative set of working space data.
- **Functionality**: Possibly uses different constraints or methods for calculating the positions, creating a new JSON file similar to `working_space.json` but with variations in the data.

### `working_space.json`
- **Purpose**: Contains the output data from `analyze.py`.
- **Content**: Lists all possible positions of the end effector for each combination of `theta1` and `theta2` angles. Serves as input for the plotting scripts to visualize the robotic arm's working space.

## Usage

1. Run `analyze.py` to generate the working space data.
2. Use `plot_workspace.py` or `plot_alt_workspace.py` to visualize the data.
3. Optionally, run `create_alt_working_space.py` to explore alternative working space configurations.

## Requirements

- Python 3.x
- Libraries: `math`, `json`, and a plotting library like `matplotlib` (if used in plotting scripts).

## License

This project is licensed under the MIT License.
