import pandas as pd

# Read CSV file
df = pd.read_csv("ML_Projects/attendance.csv")

# Calculate Attendance Percentage
df["Attendance %"] = (df["Present_Days"] / df["Total_Days"]) * 100

# Attendance Status
def status(percent):
    if percent >= 90:
        return "Excellent"
    elif percent >= 75:
        return "Good"
    elif percent >= 50:
        return "Average"
    else:
        return "Poor"

df["Status"] = df["Attendance %"].apply(status)

# Display Data
print(df)

# Statistics
print("\nAverage Attendance =", df["Attendance %"].mean())
print("Highest Attendance =", df["Attendance %"].max())
print("Lowest Attendance =", df["Attendance %"].min())