from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot normalized yearly trends
def normalized_yearly_trend(keyword: str):
    
    pytrends = TrendReq(hl='en-US', tz=360)
    
    #Set timeframe for tha data
    pytrends.build_payload([keyword], timeframe='2014-01-01 2024-12-31')  # Covers from 2018 to the end of 2024
    
    # Fetch trend data across the entire time range
    trend_data = pytrends.interest_over_time()

    # Resample to get the yearly average, which provides a comparable point per year
    yearly_trend = trend_data.resample('YE').mean()
    
    # Normalize to the maximum value across all years so that each value is relative to the peak
    yearly_trend[keyword] = (yearly_trend[keyword] / yearly_trend[keyword].max()) * 100
    
    # Reset the index to prepare for plotting
    yearly_trend.reset_index(inplace=True)
    yearly_trend['Year'] = yearly_trend['date'].dt.year
    return yearly_trend