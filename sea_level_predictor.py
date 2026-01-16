import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    x_axis = df['Year']
    y_axis = df['CSIRO Adjusted Sea Level']
    plt.scatter(x=x_axis, y=y_axis, s=1)
    
    # Create first line of best fit
    result1 = linregress(x_axis, y_axis)
    l1_x_points = pd.Series([i for i in range(1880, 2051)])
    l1_y_points = result1.slope*l1_x_points+result1.intercept
    plt.plot(l1_x_points, result1.slope*l1_x_points+result1.intercept)  
    
    # Create second line of best fit
    data_2000 = df[df['Year'] >= 2000]
    result2 = linregress(data_2000['Year'], data_2000['CSIRO Adjusted Sea Level'])
    l2_x_points = pd.Series([i for i in range(2000, 2051)])
    l2_y_points = result2.slope*l2_x_points+result2.intercept
    plt.plot(l2_x_points, l2_y_points)  
    
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()