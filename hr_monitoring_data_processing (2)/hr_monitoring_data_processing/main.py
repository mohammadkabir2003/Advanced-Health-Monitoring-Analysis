"""
The main Python module that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []  # Initialize an empty list to store the heart rate data

    # Open the file using file I/O and read it into the `data` list
    # The following code reads the file line by line and strips new lines from each line
    with open(filename, "r") as filename:
        for line in filename:
            data.append(line.strip("\n"))  # Add each line (with new line removed) to the data list
    
    # Use the `filter_nondigits` function to clean the data and remove invalid entries
    # It returns a list with only valid numeric data (converted to integers)
    data = filter_nondigits(data)
    
    # Plot the cleaned heart rate data to explore changes in heart rate over time
    # The graph will be saved to the "images" folder
    plt.plot(data)  # Plot the heart rate data
    plt.xlabel("Time (10-min intervals)")  # Label for the x-axis
    plt.ylabel("Heart Rate (BPM)")  # Label for the y-axis
    plt.savefig("images/phase3.png")  # Save the plot as a PNG image
    plt.close()  # Close the plot to free up resources

    # Calculate the average, maximum, and standard deviation of the cleaned data
    avg_hr = average(data)  # Calculate average heart rate
    max_hr = maximum(data)  # Calculate maximum heart rate
    std_dev_hr = standard_deviation(data)  # Calculate standard deviation of heart rate

    # Return the calculated metrics (average, max, and standard deviation)
    return avg_hr, max_hr, std_dev_hr


# This block will run when the script is executed directly
if __name__ == "__main__":
    print(run("data/phase3.txt"))  # Call the run function with the "phase3.txt" file and print the results
