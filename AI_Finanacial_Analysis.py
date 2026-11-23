import pandas as pd

# Load accounting data
df = pd.read_csv("AI_Accounting_Report.csv")

print("====================================")
print("       AI FINANCIAL ANALYSIS")
print("====================================")

# Calculate total values
total_taxable = df["Taxable Amount"].sum()
total_gst = df["Total GST"].sum()
total_amount = df["Total Amount"].sum()

# Average values
average_taxable = df["Taxable Amount"].mean()
average_gst = df["Total GST"].mean()
average_amount = df["Total Amount"].mean()

print("\nTotal Taxable Amount :", total_taxable)
print("Total GST            :", total_gst)
print("Total Sales Amount   :", total_amount)

print("\nAverage Taxable Amount :", average_taxable)
print("Average GST            :", average_gst)
print("Average Invoice Amount :", average_amount)

print("\n====================================")
print("            AI INSIGHT")
print("====================================")

if total_amount > 0:
    print("The business has recorded sales successfully.")

if total_gst > 0:
    print("GST has been calculated on the recorded invoices.")

print("\nNumber of Invoices :", len(df))

# Category Analysis
print("\n====================================")
print("         CATEGORY ANALYSIS")
print("====================================")

category_summary = df.groupby("Category")["Total Amount"].sum()

print("\nSales by Category:")

print(category_summary)

# Find the top category
top_category = category_summary.idxmax()
top_category_amount = category_summary.max()

print("\nTop Category :", top_category)
print("Top Category Sales :", top_category_amount)

# Customer Analysis
print("\n====================================")
print("         CUSTOMER ANALYSIS")
print("====================================")

customer_summary = df.groupby("Customer")["Total Amount"].sum()

print("\nSales by Customer:")

print(customer_summary)

# Find the top customer
top_customer = customer_summary.idxmax()
top_customer_amount = customer_summary.max()

print("\nTop Customer :", top_customer)
print("Top Customer Sales :", top_customer_amount)

# AI Financial Insights
print("\n====================================")
print("          AI FINANCIAL INSIGHTS")
print("====================================")

# Category insight
print(
    "\nAI Insight: Your highest-performing category is",
    top_category,
    "with sales of",
    top_category_amount
)

# Customer insight
print(
    "AI Insight: Your top customer is",
    top_customer,
    "with total sales of",
    top_customer_amount
)

# GST insight
if total_gst > 0:
    print("AI Insight: GST is being generated from your recorded invoices.")

# Invoice insight
if len(df) >= 5:
    print("AI Insight: You have", len(df), "invoices recorded in the system.")
else:
    print("AI Insight: Add more invoices to improve the analysis.")


# Final Accounting Summary
print("\n====================================")
print("      FINAL AI ACCOUNTING SUMMARY")
print("====================================")

print("\nTotal Invoices      :", len(df))
print("Total Sales         :", total_amount)
print("Total GST           :", total_gst)
print("Top Category        :", top_category)
print("Top Customer        :", top_customer)

print("\n------------------------------------")
print("AI analysis is based on the current")
print("accounting records in the CSV file.")
print("------------------------------------")

print("\n====================================")
print("     STEP 8 COMPLETED SUCCESSFULLY")
print("====================================")
