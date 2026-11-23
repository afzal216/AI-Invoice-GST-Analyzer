import pandas as pd

# Load accounting data
df = pd.read_csv("AI_Accounting_Report.csv")

print("====================================")
print("          INVOICE SEARCH")
print("====================================")

invoice_no = input("\nEnter Invoice Number: ")

# Search for invoice
result = df[df["Invoice No"].astype(str).str.upper() == invoice_no.upper()]

if not result.empty:
    print("\nInvoice Found!")
    print("------------------------------------")
    print(result.to_string(index=False))
else:
    print("\nInvoice not found.")

print("\n====================================")
print("        SEARCH COMPLETED")
print("====================================")
