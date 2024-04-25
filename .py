import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv", float_precision="legacy").rename(
        columns={
            "Year": "year",
            "CSIRO Adjusted Sea Level": "sea",
        }
    )
  
    # Create scatter plot
    plt.figure(1, figsize=(16, 9))
    plt.scatter(df["year"], df["sea"])

    # Create first line of best fit
    regress = linregress(df["year"], df["sea"])
    last_year = df["year"].max()
    df_ext = pd.DataFrame({"year": range(last_year + 1, 2051)})
    df = pd.concat([df, df_ext], ignore_index=True)
    plt.plot(
        df["year"],
        regress.intercept + regress.slope * df["year"],
        c="r",
        label="fit all",
    )

    # Create second line of best fit
    df_recent = df.loc[df["year"] >= 2000]
    df_recent = df_recent.dropna()  # Filter out null values
    bestfit = linregress(df_recent["year"], df_recent["sea"])
    df_ext_recent = pd.DataFrame({"year": range(last_year + 1, 2051)})  # Exclude the missing year
    df_recent = pd.concat([df_recent, df_ext_recent], ignore_index=True)
    plt.plot(
        df_recent["year"],
        bestfit.intercept + bestfit.slope * df_recent["year"],
        c="b",
        label="fit recent",
    )

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

