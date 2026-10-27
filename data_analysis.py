import pandas as pd

# Student performance data
data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Marks": [85, 92, 67, 78, 95]
}

df = pd.DataFrame(data)

print("Student Performance Data:")
print(df)

average = df["Marks"].mean()
print("\nAverage Marks:", average)

topper = df.loc[df["Marks"].idxmax()]
print("\nTopper:", topper["Name"])
print("Topper Marks:", topper["Marks"])
