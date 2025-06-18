import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    fig, ax = plt.subplots()
    plt.scatter(x, y, color='blue', label='Data points')

    # Create first line of best fit 
    lin_reg = linregress(x,y) # Perform linear regression
    print(lin_reg)
    x_ax = pd.Series([i for i in range(1880,2051)])
    y_ec = lin_reg.slope*x_ax + lin_reg.intercept
    plt.plot(x_ax, y_ec, color='purple')
    

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing 
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()