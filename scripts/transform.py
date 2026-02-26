import pandas as pd
from extract import extract_towns, extract_weather_data

def printDFSummary(dataFrame):
    print(dataFrame.info())
    print("\n----------")
    print(dataFrame.head())
    print("\n----------")
    print(dataFrame.describe())
    print("\n----------")
    print(dataFrame.isna().sum())
    print("\n----------")
    print("\n----------")

def transform_towns():
    towns_data = extract_towns()
    townsDataDF = pd.DataFrame(towns_data)
    return townsDataDF


def transform_weather_data():
    weather_data = extract_weather_data()
    weatherDataDF = pd.DataFrame(weather_data)
    return weatherDataDF


def mergeData(df1, df2):
    mergedDF = df1.merge(df2, left_index=True, right_index=True)
    return mergedDF



df1 = transform_towns()
df2 = transform_weather_data()

mergedDF = mergeData(df1, df2)
