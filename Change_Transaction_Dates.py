import csv

file_name = "AI_Accounting_Report.csv"

dates = {
    "INV001": "2026-06-25",
    "INV002": "2026-07-23",
    "INV003": "2026-08-18",
    "INV004": "2026-09-30"
}

# Read the existing report
with open(file_name, "r", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    fieldnames = reader.fieldnames

# Change only the dates
for row in rows:
    invoice = row["Invoice No"]

    if invoice in dates:
        row["Date"] = dates[invoice]

# Save the updated report
with open(file_name, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print("===================================")
print("Transaction dates updated!")
print("===================================")

for invoice, date in dates.items():
    print(invoice, "->", date)

print("\nAI_Accounting_Report.csv updated successfully!")
