import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv").head()
    print(df)
    # Create scatter plot
    

    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing 
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()