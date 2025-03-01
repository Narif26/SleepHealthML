import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

#print(df.head())

#print(df.isnull().sum())

#print(df.info())

print(df.describe())