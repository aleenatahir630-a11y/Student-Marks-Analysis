import pandas as pd

# Student data
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Marks": [80, 90, 75, 95, 70]
}

# Create DataFrame
df = pd.DataFrame(data)

# Assign grades
df["Grade"] = ["A", "A+", "B", "A+", "B"]

# Display student results
print("Student Results:")
print(df)

# Calculate statistics
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

print("\nAnalysis:")
print("Average Marks =", average_marks)
print("Highest Marks =", highest_marks)
print("Lowest Marks =", lowest_marks)

# Save results to CSV
df.to_csv("students_results.csv", index=False)

print("\nCSV file created successfully!")
