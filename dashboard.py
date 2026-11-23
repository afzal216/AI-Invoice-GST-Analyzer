import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


print("======================================")
print("      AI ACCOUNTING DASHBOARD")
print("======================================")


# ======================================
# ACCOUNTING REPORT
# ======================================

file_name = "AI_Accounting_Report.csv"

if not os.path.exists(file_name):

    print("No accounting report found!")
    print("Please add transactions first.")

else:

    total_amount = 0
    total_gst = 0
    total_sales = 0
    total_expenses = 0
    transaction_count = 0

    with open(file_name, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            amount = float(row["Taxable Amount"])
            gst = float(row["Total GST"])
            category = row["Category"]

            total_amount += amount
            total_gst += gst
            transaction_count += 1

            # Identify sales
            if category == "Sales":
                total_sales += amount

            # Identify expenses
            else:
                total_expenses += amount


    # Calculate profit/loss
    profit = total_sales - total_expenses


    # ======================================
# AI FINANCIAL SUMMARY
# ======================================

prediction_report = "AI_Financial_Prediction_Report.csv"

if os.path.exists(prediction_report):

    prediction_df = pd.read_csv(prediction_report)

    print("\n================================================")
    print("             AI FINANCIAL SUMMARY")
    print("================================================")

    print("Financial Trend        :", prediction_df["Financial Trend"].iloc[0])
    print("Financial Health Score :", prediction_df["Financial Health Score"].iloc[0])
    print("Financial Health Status:", prediction_df["Financial Health Status"].iloc[0])

    print("Total Income           : ₹", prediction_df["Total Income"].iloc[0])
    print("Total Expenses         : ₹", prediction_df["Total Expenses"].iloc[0])
    print("Net Position           : ₹", prediction_df["Net Position"].iloc[0])

    print("Best Performing Month :", prediction_df["Best Performing Month"].iloc[0])
    print("Lowest Performing Month :", prediction_df["Lowest Performing Month"].iloc[0])
print("\nAI Financial Insight:")
print(prediction_df["AI Financial Insight"].iloc[0])


# ======================================
# AI BUSINESS RECOMMENDATION
# ======================================

health_score = float(
    prediction_df["Financial Health Score"].iloc[0]
)

trend = str(
    prediction_df["Financial Trend"].iloc[0]
).upper()

net_position = float(
    prediction_df["Net Position"].iloc[0]
)

if net_position < 0:

    business_recommendation = (
        "Expenses are higher than income. "
        "The business should reduce unnecessary expenses "
        "and focus on increasing sales."
    )

elif health_score < 50:

    business_recommendation = (
        "Financial health needs attention. "
        "The business should closely monitor expenses, "
        "cash flow and future transactions."
    )

elif trend == "DECREASING":

    business_recommendation = (
        "The financial trend is decreasing. "
        "The business should improve sales performance "
        "and control operating expenses."
    )

elif health_score >= 75 and net_position > 0:

    business_recommendation = (
        "The business is financially healthy. "
        "Maintain the current performance while "
        "continuing to monitor future trends."
    )

else:

    business_recommendation = (
        "The financial position is moderate. "
        "Continue monitoring income, expenses and "
        "future transaction trends."
    )


print("\nAI Business Recommendation:")
print(business_recommendation)

print("================================================")


    # ======================================
    # AI FINANCIAL PREDICTION
    # ======================================

prediction_file = "financial_data.csv"

if os.path.exists(prediction_file):

        df = pd.read_csv(prediction_file)

        # Create numerical month numbers
        df["MonthNumber"] = range(1, len(df) + 1)

        X = df[["MonthNumber"]]

        # -----------------------------
        # Sales prediction
        # -----------------------------

        sales_model = LinearRegression()

        sales_model.fit(X, df["Sales"])

        future_month = pd.DataFrame(
            {"MonthNumber": [len(df) + 1]}
        )

        predicted_sales = sales_model.predict(
            future_month
        )[0]


        # -----------------------------
        # Expense prediction
        # -----------------------------

        expense_model = LinearRegression()

        expense_model.fit(X, df["Expenses"])

        predicted_expenses = expense_model.predict(
            future_month
        )[0]


        # -----------------------------
        # Profit/Loss prediction
        # -----------------------------

        predicted_profit = (
            predicted_sales - predicted_expenses
        )


        # ======================================
        # AI FORECAST
        # ======================================

        print("\n========== AI FORECAST ==========")

        print(
            "Predicted Sales       : ₹",
            round(predicted_sales, 2)
        )

        print(
            "Predicted Expenses    : ₹",
            round(predicted_expenses, 2)
        )


        if predicted_profit > 0:

            print(
                "Predicted Profit      : ₹",
                round(predicted_profit, 2)
            )

        elif predicted_profit < 0:

            print(
                "Predicted Loss        : ₹",
                round(abs(predicted_profit), 2)
            )

        else:

            print("Predicted Break-even  : ₹0")


        print("================================")


        # ======================================
        # CHART 1 - SALES VS EXPENSES
        # ======================================

        labels = ["Sales", "Expenses"]
        values = [total_sales, total_expenses]

        plt.figure(figsize=(7, 5))

        plt.bar(labels, values)

        plt.title("Sales vs Expenses")
        plt.xlabel("Category")
        plt.ylabel("Amount (₹)")

        plt.show()


        # ======================================
        # CHART 2 - CURRENT PROFIT / LOSS
        # ======================================

        plt.figure(figsize=(7, 5))

        if profit > 0:

            label = "Profit"
            title = "Estimated Profit"

        elif profit < 0:

            label = "Loss"
            title = "Estimated Loss"

        else:

            label = "Break-even"
            title = "Break-even"

        plt.bar(
            [label],
            [abs(profit)]
        )

        plt.title(title)
        plt.xlabel("Financial Result")
        plt.ylabel("Amount (₹)")

        plt.show()


        # ======================================
        # CHART 3 - AI FORECAST
        # ======================================

        months = list(df["MonthNumber"]) + [
            len(df) + 1
        ]

        sales_values = list(df["Sales"]) + [
            predicted_sales
        ]

        expense_values = list(df["Expenses"]) + [
            predicted_expenses
        ]


        plt.figure(figsize=(9, 6))

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
            x=len(df) + 0.5,
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


else:

        print("\nAI prediction data not found.")

        print(
            "Please make sure financial_data.csv exists."
        )
