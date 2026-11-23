import pandas as pd

# Historical financial data
data = {
    "Month": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October"
    ],

    "Sales": [
        50000,
        55000,
        60000,
        58000,
        65000,
        70000,
        68000,
        75000,
        80000,
        85000
    ],

    "Expenses": [
        30000,
        32000,
        35000,
        34000,
        37000,
        40000,
        39000,
        42000,
        45000,
        47000
    ]
}

df = pd.DataFrame(data)

# Calculate profit
df["Profit"] = df["Sales"] - df["Expenses"]

print("Historical Financial Data")
print("-------------------------")
print(df)

df.to_csv("financial_data.csv",index=False)
print("Financial data saved successfully!")
