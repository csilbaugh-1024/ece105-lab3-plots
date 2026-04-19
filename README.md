<!-- Create a README.md with these sections:
     1. Project title and one-sentence description
     2. Installation (activate ece105 conda env, pip install numpy matplotlib)
     3. Usage (python generate_plots.py)
     4. Example output (describe the three plots briefly)
     5. AI tools used and disclosure -->

# Lab 3: Sensor Data Visualization

A Python script that generates synthetic temperature sensor data and produces publication-quality visualizations to analyze sensor distributions and readings over time.

## Installation

1. Activate the `ece105` conda environment:
   ```bash
   conda activate ece105
   ```

2. Install required dependencies:
   ```bash
   conda install numpy matplotlib
   ```
   Or with mamba:
   ```bash
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the command line:

```bash
python generate_plots.py
```

The script generates synthetic temperature data from two sensors and creates visualizations.

## Example Output

The script generates `sensor_analysis.png`, a figure containing three subplots:

1. **Scatter Plot**: Temperature readings vs. time for both sensors. Sensor A is shown in blue and Sensor B in orange, with both overlaid on the same axes to compare temporal patterns.

2. **Histogram**: Overlaid distribution of temperature readings from both sensors. Shows the frequency of each temperature range with 30 bins. Vertical dashed lines mark each sensor's mean temperature.

3. **Box Plot**: Side-by-side comparison of sensor temperature distributions. Displays median, quartiles, and outliers for each sensor, with a red dashed line indicating the overall mean of both sensors combined.

## AI Tools Used and Disclosure

This project was developed with assistance from GitHub Copilot Chat within VS Code. 
Copilot was used to generate initial code for data generation, plotting functions, 
and the main() entry point based on intent comments written beforehand. All generated 
code was reviewed, understood, and modified where necessary before use. The "explain first" pattern was followed throughout — intent comments were written before prompting the AI, and those comments remain in the code as documentation. Furthermore, Claude was used to clarify
certain steps in the lab when needed, though it generated no code.
