import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
The data I used to train the model is california housing price(large data set)
Note the TARGET variable is median_house_value
"""

dataset = pd.read_csv("housing.csv")

#print(dataset.head(50))

dataset.dropna(inplace=True)
dataset.info()