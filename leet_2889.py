'''Pivot data so that each row represents temps for specific month,
each city is a separate column'''
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')
