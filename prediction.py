import pandas as pd
from sklearn.linear_model import LinearRegression

# Read accounting data from CSV
df = pd.read_csv("financial_data.csv")
df["MonthNumber"] = range(1, len(df) + 1)

print("Accounting data loaded successfully!")
print()

# -----------------------------
# Sales Prediction
# -----------------------------

sales_model = LinearRegression()

X = df[["MonthNumber"]]
sales_y = df["Sales"]

sales_model.fit(X, sales_y)

future_month = pd.DataFrame({"MonthNumber": [11]})

predicted_sales = sales_model.predict(future_month)[0]

# -----------------------------
# Expense Prediction
# -----------------------------

expense_model = LinearRegression()

expense_y = df["Expenses"]

expense_model.fit(X, expense_y)

predicted_expenses = expense_model.predict(future_month)[0]

# -----------------------------
# Profit Prediction
# -----------------------------

predicted_profit = predicted_sales - predicted_expenses

# -----------------------------
# Display Results
# -----------------------------

print("AI Financial Prediction")
print("-----------------------")

print("Predicted Sales for Month 11:")
print(round(predicted_sales, 2))

print()

print("Predicted Expenses for Month 11:")
print(round(predicted_expenses, 2))

print()

if predicted_profit > 0:
    print("Predicted Profit for Month 11:")
    print("₹", round(predicted_profit, 2))

elif predicted_profit < 0:
    print("Predicted Loss for Month 11:")
    print("₹", round(abs(predicted_profit), 2))

else:
    print("Month 11 is predicted to Break Even")
    print("Profit/Loss: ₹0")
