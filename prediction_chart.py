import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load accounting data
df = pd.read_csv("financial_data.csv")

# Create numerical month numbers
df["MonthNumber"] = range(1, len(df) + 1)

# -----------------------------
# Sales prediction
# -----------------------------

X = df[["MonthNumber"]]
sales_y = df["Sales"]

sales_model = LinearRegression()
sales_model.fit(X, sales_y)

future_month = pd.DataFrame({"MonthNumber": [11]})
predicted_sales = sales_model.predict(future_month)[0]

# -----------------------------
# Expense prediction
# -----------------------------

expense_y = df["Expenses"]

expense_model = LinearRegression()
expense_model.fit(X, expense_y)

predicted_expenses = expense_model.predict(future_month)[0]

# -----------------------------
# Create chart data
# -----------------------------

months = list(df["MonthNumber"]) + [11]

sales_values = list(df["Sales"]) + [predicted_sales]
expense_values = list(df["Expenses"]) + [predicted_expenses]

# -----------------------------
# Create chart
# -----------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    months,
    sales_values,
    marker="o",
    label="Sales"
)

plt.plot(
    months,
    expense_values,
    marker="o",
    label="Expenses"
)

plt.axvline(
    x=10.5,
    linestyle="--",
    label="AI Prediction"
)

plt.title("AI Financial Prediction")
plt.xlabel("Month")
plt.ylabel("Amount (₹)")

plt.xticks(months)

plt.legend()
plt.grid(True)

plt.show()
