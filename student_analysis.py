import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Marks": [80, 90, 75, 95, 70]
}

df = pd.DataFrame(data)

print(df)

print("\nAverage Marks =", df["Marks"].mean())
print("Highest Marks =", df["Marks"].max())
print("Lowest Marks =", df["Marks"].min())
import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"],
    "Marks": [80, 90, 75, 95, 70]
}

df = pd.DataFrame(data)

df["Grade"] = ["A", "A+", "B", "A+", "B"]

print(df)
import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

print("CSV file created successfully!")