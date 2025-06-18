import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    fig, ax = plt.subplots() # Verify doc
    plt.scatter(x, y, color='blue', label='Data points')

    # Create first line of best fit 
    lin_reg = linregress(x,y) # Perform linear regression
    print(lin_reg)
    x_ax = pd.Series([i for i in range(1880,2051)])
    y_fit1 = lin_reg.slope*x_ax + lin_reg.intercept
    plt.plot(x_ax, y_fit1, color='purple')
    
    # Create second line of best fit
    new_ax = df.loc[df['Year'] >= 2000]
    X = new_ax["Year"]
    Y = new_ax["CSIRO Adjusted Sea Level"]
    lin_reg2 = linregress(X,Y)
    x_ax2 = pd.Series([i for i in range(2000,2051)])
    Y_fit2 = lin_reg2.slope*x_ax2 + lin_reg2.intercept
    plt.plot(x_ax2, Y_fit2, color='green')
    
    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level - Inches")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing 
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()