# Zomato Rider Performance Analysis
# Author: Deepesh Siwach
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("zomato_rider_performance_dataset.csv")
print("✅ Data Loaded Successfully!")
print(df.head(), "\n")

# Basic info
print("Dataset shape:", df.shape)
print("\nMissing Values:\n", df.isna().sum())

# City-wise distribution
print("\nRiders per City:\n", df['City'].value_counts())

# --- Correlation Heatmap ---
plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include=['number']).corr(),
            annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Heatmap (Numeric Features Only)")
plt.show()
plt.title("Correlation Heatmap of Key Metrics")
plt.show()

# --- Deliveries vs Active Hours ---
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Active_Hours', y='Total_Deliveries', hue='City')
plt.title("Deliveries vs Active Hours by City")
plt.show()

# --- Salary Distribution ---
plt.figure(figsize=(8,5))
sns.histplot(df['Salary'], bins=20, kde=True)
plt.title("Salary Distribution of Riders")
plt.show()

# --- Ratings by City ---
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='City', y='Customer_Rating')
plt.title("Customer Ratings by City")
plt.show()

# --- Create Summary File for Power BI ---
summary = df.groupby('City').agg({
    'Rider_ID': 'count',
    'Total_Deliveries': 'mean',
    'Customer_Rating': 'mean',
    'Salary': 'mean',
    'NPT_Percent': 'mean'
}).reset_index()

summary.rename(columns={'Rider_ID': 'Rider_Count'}, inplace=True)
summary.to_csv("zomato_rider_city_summary.csv", index=False)
print("\n✅ Summary file created: zomato_rider_city_summary.csv")
print(summary)


# ---- Final Step: Export Clean Data for Power BI ----

# 1️⃣ Choose only useful columns for Power BI
columns_to_keep = [
    'Rider_ID', 
    'Total_Deliveries', 
    'Total_Calls', 
    'Active_Hours',
    'Attendance_Percent', 
    'Customer_Rating', 
    'Delivery_Time_Min',
    'Deliveries_Per_Hour', 
    'NPT_Percent', 
    'Salary'
]

# 2️⃣ Create a new DataFrame with those columns
clean_df = df[columns_to_keep]

# 3️⃣ Save (export) this clean data into a new CSV file
clean_df.to_csv("cleaned_zomato_rider_data.csv", index=False)

# 4️⃣ Confirm it's saved
print("✅ Clean dataset exported successfully as 'cleaned_zomato_rider_data.csv'")

