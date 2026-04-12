import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, Label
from sklearn.impute import SimpleImputer
# Load the Titanic dataset
df = pd.read_csv('train.csv')
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())