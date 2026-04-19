"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

def generate_data(seed):
    """Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random number generator seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    """
    rng = np.random.default_rng(seed=seed)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    return sensor_a, sensor_b, timestamps


# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.



def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot sensor readings as a scatter plot over time.
    
    Draws scatter points for both sensors with distinct colors and transparency,
    modifying the Axes object in place.
    
    Parameters
    ----------
    sensor_a : ndarray, shape (200,)
        Temperature readings from sensor A in Celsius.
    sensor_b : ndarray, shape (200,)
        Temperature readings from sensor B in Celsius.
    timestamps : ndarray, shape (200,)
        Measurement timestamps in seconds.
    ax : matplotlib.axes.Axes
        Axes object to modify in place.
    
    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.6)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.6)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (C)')
    ax.set_title('Sensor Readings Over Time')
    ax.legend()
    ax.grid(True, alpha=0.3)

