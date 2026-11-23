import pandas as pd

print("================================================")
print("        AI FINANCIAL PREDICTION SYSTEM")
print("================================================")

# ------------------------------------------------
# 1. LOAD ACCOUNTING DATA
# ------------------------------------------------

file_name = "AI_Accounting_Report.csv"

df = pd.read_csv(file_name)

# Clean column names
df.columns = df.columns.str.strip()

# Convert data types
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Total Amount"] = pd.to_numeric(
    df["Total Amount"], errors="coerce"
)

# Remove invalid transactions
df = df.dropna(subset=["Date", "Total Amount"])

# Sort by date
df = df.sort_values("Date").reset_index(drop=True)

# ------------------------------------------------
# 2. CHECK TRANSACTIONS
# ------------------------------------------------

print("\nTotal Transactions:", len(df))

print("\nTRANSACTION HISTORY")
print("------------------------------------------------")

for _, row in df.iterrows():
    print(
        row["Invoice No"],
        "|",
        row["Date"].date(),
        "| ₹",
        round(row["Total Amount"], 2)
    )

# ------------------------------------------------
# 3. BASIC FINANCIAL ANALYSIS
# ------------------------------------------------

amounts = df["Total Amount"]

highest_amount = amounts.max()
lowest_amount = amounts.min()
average_amount = amounts.mean()

highest_invoice = df.loc[
    df["Total Amount"].idxmax(), "Invoice No"
]

lowest_invoice = df.loc[
    df["Total Amount"].idxmin(), "Invoice No"
]

# ------------------------------------------------
# 4. CALCULATE TIME BETWEEN TRANSACTIONS
# ------------------------------------------------

df["Days_Between"] = df["Date"].diff().dt.days

average_days = df["Days_Between"].dropna().mean()

# ------------------------------------------------
# 5. CALCULATE FINANCIAL TREND
# ------------------------------------------------

if len(df) >= 2:

    # Convert dates to numbers
    first_date = df["Date"].min()

    df["Date_Number"] = (
        df["Date"] - first_date
    ).dt.days

    x = df["Date_Number"]
    y = df["Total Amount"]

    x_mean = x.mean()
    y_mean = y.mean()

    numerator = (
        (x - x_mean) *
        (y - y_mean)
    ).sum()

    denominator = (
        (x - x_mean) ** 2
    ).sum()

    if denominator != 0:
        slope = numerator / denominator
    else:
        slope = 0

    intercept = y_mean - (slope * x_mean)

else:

    slope = 0
    intercept = amounts.iloc[0]

# ------------------------------------------------
# 6. PREDICT NEXT TRANSACTION DATE
# ------------------------------------------------

last_date = df["Date"].max()

if pd.isna(average_days) or average_days <= 0:
    average_days = 30

predicted_date = (
    last_date +
    pd.Timedelta(days=round(average_days))
)

# ------------------------------------------------
# 7. PREDICT NEXT TRANSACTION AMOUNT
# ------------------------------------------------

future_day = (
    predicted_date - first_date
).days

predicted_amount = (
    intercept +
    slope * future_day
)

# Prevent negative prediction
if predicted_amount < 0:
    predicted_amount = 0

# ------------------------------------------------
# 8. DETERMINE TREND
# ------------------------------------------------

if slope > 0:
    trend = "INCREASING"

elif slope < 0:
    trend = "DECREASING"

else:
    trend = "STABLE"


# ------------------------------------------------
# 9A. AI FINANCIAL HEALTH SCORE
# ------------------------------------------------

score = 50

# Trend factor
if slope > 0:
    score += 20
elif slope < 0:
    score -= 20

# Transaction consistency
if len(df) >= 3:

    amount_std = amounts.std()
    consistency_ratio = amount_std / average_amount

    if consistency_ratio < 0.30:
        score += 20

    elif consistency_ratio < 0.60:
        score += 10

    else:
        score -= 10

# Recent transaction compared with average
last_amount = amounts.iloc[-1]

if last_amount >= average_amount:
    score += 10
else:
    score -= 5

# Keep score between 0 and 100
score = max(0, min(100, score))

# Determine health level
if score >= 75:
    health_status = "HEALTHY"

elif score >= 50:
    health_status = "MODERATE"

else:
    health_status = "NEEDS ATTENTION"
# ------------------------------------------------
# 9B. AUTOMATIC UNUSUAL TRANSACTION DETECTION
# ------------------------------------------------

median_amount = amounts.median()

unusual_transactions = []

for index, row in df.iterrows():

    transaction_amount = float(row["Total Amount"])

    # Detect transactions significantly higher than
    # the normal transaction level
    if transaction_amount > median_amount * 2:

        unusual_transactions.append({
            "invoice": row["Invoice No"],
            "amount": transaction_amount
        })

if len(unusual_transactions) > 0:
    anomaly_status = "UNUSUAL TRANSACTION DETECTED"
else:
    anomaly_status = "NO MAJOR UNUSUAL TRANSACTIONS"
# ------------------------------------------------
# 9C. SMART AI FINANCIAL RECOMMENDATION
# ------------------------------------------------

recommendations = []

# Trend recommendation
if slope > 0:
    recommendations.append(
        "Transaction values are increasing. "
        "Monitor cash flow as business activity grows."
    )

elif slope < 0:
    recommendations.append(
        "Transaction values are decreasing. "
        "Review sales activity and expenses."
    )

else:
    recommendations.append(
        "Transaction values are relatively stable. "
        "Continue monitoring financial activity."
    )

# Health score recommendation
if score >= 75:
    recommendations.append(
        "Financial health is strong. Maintain the current performance."
    )

elif score >= 50:
    recommendations.append(
        "Financial health is moderate. Improve transaction consistency."
    )

else:
    recommendations.append(
        "Financial health needs attention. Review expenses and cash flow."
    )

# Unusual transaction recommendation
if len(unusual_transactions) > 0:

    recommendations.append(
        "An unusual transaction was detected. "
        "Review the flagged invoice before making financial decisions."
    )

# Combine recommendations
recommendation = " ".join(recommendations)
# ------------------------------------------------
# 9D. MONTHLY FINANCIAL SUMMARY
# ------------------------------------------------

df["Month"] = df["Date"].dt.to_period("M")

monthly_summary = (
    df.groupby("Month")["Total Amount"]
    .agg(["sum", "mean", "count"])
    .reset_index()
)

monthly_summary.columns = [
    "Month",
    "Total Amount",
    "Average Amount",
    "Transactions"
]

best_month = monthly_summary.loc[
    monthly_summary["Total Amount"].idxmax()
]

lowest_month = monthly_summary.loc[
    monthly_summary["Total Amount"].idxmin()
]

# ------------------------------------------------
# DISPLAY MONTHLY SUMMARY
# ------------------------------------------------

print("\n================================================")
print("          MONTHLY FINANCIAL SUMMARY")
print("================================================")

for _, row in monthly_summary.iterrows():

    print(
        row["Month"],
        "| Total: ₹",
        round(row["Total Amount"], 2),
        "| Average: ₹",
        round(row["Average Amount"], 2),
        "| Transactions:",
        int(row["Transactions"])
    )

print("\nBest Performing Month :",
      best_month["Month"],
      "| ₹",
      round(best_month["Total Amount"], 2))

print("Lowest Performing Month :",
      lowest_month["Month"],
      "| ₹",
      round(lowest_month["Total Amount"], 2))

print("================================================")
# ------------------------------------------------
# 9E. AI INCOME VS EXPENSE ANALYSIS
# ------------------------------------------------

# Identify income transactions
income_df = df[
    df["Category"].str.strip().str.lower() == "sales"
]

# All non-sales transactions are treated as expenses
expense_df = df[
    df["Category"].str.strip().str.lower() != "sales"
]

total_income = income_df["Total Amount"].sum()
total_expenses = expense_df["Total Amount"].sum()

net_position = total_income - total_expenses

# Generate AI financial insight
if total_income > total_expenses:

    financial_insight = (
        "Income is higher than expenses. "
        "The business has a positive financial position."
    )

elif total_income < total_expenses:

    financial_insight = (
        "Expenses are higher than income. "
        "The business should review its spending and cash flow."
    )

else:

    financial_insight = (
        "Income and expenses are equal. "
        "The business has a neutral financial position."
    )

# ------------------------------------------------
# DISPLAY INCOME VS EXPENSE ANALYSIS
# ------------------------------------------------

print("\n================================================")
print("          AI INCOME VS EXPENSE ANALYSIS")
print("================================================")

print("Total Income   : ₹", round(total_income, 2))
print("Total Expenses : ₹", round(total_expenses, 2))
print("Net Position   : ₹", round(net_position, 2))

print("\nAI Financial Insight:")
print(financial_insight)

print("================================================")
# ------------------------------------------------
# 10. DISPLAY AI ANALYSIS
# ------------------------------------------------

print("\n================================================")
print("             FINANCIAL ANALYSIS")
print("================================================")

print("Highest Transaction :", highest_invoice,
      "| ₹", round(highest_amount, 2))

print("Lowest Transaction  :", lowest_invoice,
      "| ₹", round(lowest_amount, 2))

print("Average Transaction : ₹",
      round(average_amount, 2))

print("Average Days Between Transactions :",
      round(average_days, 2))

print("\nFinancial Trend :", trend)

print("Financial Health Score :", score, "/ 100")
print("Financial Health Status:", health_status)
print("Unusual Transaction Check:", anomaly_status)

if len(unusual_transactions) > 0:

    print("\nWARNING - UNUSUAL TRANSACTIONS:")

    for transaction in unusual_transactions:

        print(
            transaction["invoice"],
            "| ₹",

            round(transaction["amount"], 2)

        )

# ------------------------------------------------
# 11. DISPLAY PREDICTION
# ------------------------------------------------

print("\n================================================")
print("              AI PREDICTION")
print("================================================")

print("Last Transaction Date :",
      last_date.date())

print("Predicted Next Date   :",
      predicted_date.date())

print("Predicted Amount      : ₹",
      round(predicted_amount, 2))

print("\nAI Recommendation:")
print(recommendation)

print("================================================")

# ------------------------------------------------
# 12. SAVE PREDICTION REPORT
# ------------------------------------------------

prediction_data = {
    "Unusual Transaction Check": [anomaly_status],
    "Last Transaction Date": [last_date.date()],
    "Predicted Next Date": [predicted_date.date()],
    "Total Transactions": [len(df)],
    "Average Transaction": [round(average_amount, 2)],
    "Highest Transaction": [round(highest_amount, 2)],
    "Lowest Transaction": [round(lowest_amount, 2)],
    "Average Days Between Transactions": [
        round(average_days, 2)
    ],
    "Financial Trend": [trend],

    "Total Income": [round(total_income, 2)],
    "Total Expenses": [round(total_expenses, 2)],
    "Net Position": [round(net_position, 2)],
    "AI Financial Insight":[financial_insight],
    "Best Performing Month": [str(best_month["Month"])],
    "Lowest Performing Month": [str(lowest_month["Month"])],
    
    "Financial Health Score": [score],
    "Financial Health Status": [health_status],
    
    "Predicted Next Amount": [
        round(predicted_amount, 2)
    ],
    "AI Recommendation": [recommendation]
}

prediction_df = pd.DataFrame(prediction_data)

prediction_df.to_csv(
    "AI_Financial_Prediction_Report.csv",
    index=False
)

print("\nPrediction report saved successfully!")
print("File: AI_Financial_Prediction_Report.csv")

print("\n===================================")
print("       AI PREDICTION RESULT")
print("===================================")

print("Financial Trend       :", trend)
print("Financial Health Score:", score)
print("Financial Health      :", health_status)
print("Predicted Next Date   :", predicted_date.date())
print("Predicted Next Amount :", round(predicted_amount, 2))
print("AI Recommendation     :", recommendation)

print("===================================")
