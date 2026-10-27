import pandas as pd

# Student performance data
data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Marks": [85, 92, 67, 78, 95]
}

df = pd.DataFrame(data)

# Display student data
print("Student Performance Data:")
print(df)

# Calculate average marks
average = df["Marks"].mean()
print("\nAverage Marks:", average)

# Find the topper
topper = df.loc[df["Marks"].idxmax()]
print("\nTopper:", topper["Name"])
print("Topper Marks:", topper["Marks"])
