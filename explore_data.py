import pandas as pd

# Dataset ka naam yahan change karen apne file ke hisaab se
data = pd.read_csv("dataset.csv")  

# Pehle 5 rows dekhna
print("First 5 rows of the dataset:")
print(data.head())

# Column names check karna
print("\nColumns in the dataset:")
print(data.columns)

# Dataset ka shape (rows aur columns ka count)
print("\nDataset shape (rows, columns):")
print(data.shape)
