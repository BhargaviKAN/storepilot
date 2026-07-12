from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/raw/store_performance.csv")

df = pd.read_csv(DATA_PATH)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst five rows:")
print(df.head())
print("\nMissing values:")
print(df.isna().sum())
print("\nSummary:")
print(df.describe(include="all"))
