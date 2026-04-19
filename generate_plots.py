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

# Create plot_histogram(sensor_a, sensor_b, ax) that draws the overlaid
# histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid histogram of sensor temperature distributions.
    
    Draws overlapping histograms for both sensors with vertical lines
    marking each sensor's mean, modifying the Axes object in place.
    
    Parameters
    ----------
    sensor_a : ndarray, shape (200,)
        Temperature readings from sensor A in Celsius.
    sensor_b : ndarray, shape (200,)
        Temperature readings from sensor B in Celsius.
    ax : matplotlib.axes.Axes
        Axes object to modify in place.
    
    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='blue')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='orange')
    ax.axvline(sensor_a.mean(), color='blue', linestyle='--', linewidth=2,
               label=f'Sensor A mean: {sensor_a.mean():.2f}C')
    ax.axvline(sensor_b.mean(), color='orange', linestyle='--', linewidth=2,
               label=f'Sensor B mean: {sensor_b.mean():.2f}C')
    ax.set_xlabel('Temperature (C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distribution: Sensor A vs Sensor B')
    ax.legend()
    ax.grid(True, alpha=0.3)

# Create plot_boxplot(sensor_a, sensor_b, ax) that draws the side-by-side
# box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_boxplot(sensor_a, sensor_b, ax):
    """Plot side-by-side box plots of sensor temperature distributions.
    
    Draws box plots for both sensors with a horizontal line marking the
    overall mean of both sensors combined, modifying the Axes object in place.
    
    Parameters
    ----------
    sensor_a : ndarray, shape (200,)
        Temperature readings from sensor A in Celsius.
    sensor_b : ndarray, shape (200,)
        Temperature readings from sensor B in Celsius.
    ax : matplotlib.axes.Axes
        Axes object to modify in place.
    
    Returns
    -------
    None
    """
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    
    ax.boxplot([sensor_a, sensor_b], tick_labels=['Sensor A', 'Sensor B'])
    ax.axhline(overall_mean, color='red', linestyle='--', linewidth=2,
               label=f'Overall mean: {overall_mean:.2f}C')
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Temperature Distribution: Sensor A vs Sensor B')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main():
    """Generate synthetic sensor data and create publication-quality plots.
    
    Generates temperature sensor readings, creates a figure with three subplots
    (scatter, histogram, and box plot), and saves the figure as a PNG file.
    
    Returns
    -------
    None
    """
    sensor_a, sensor_b, timestamps = generate_data(seed=5074)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])
    
    plt.tight_layout()
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    print("Saved sensor_analysis.png")
    plt.close()


if __name__ == '__main__':
    main()
