import csv

file_name = "AI_Accounting_Report.csv"

# Read existing accounting data
with open(file_name, "r", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    old_fieldnames = reader.fieldnames

# Add Date column after Invoice No
new_fieldnames = []

for field in old_fieldnames:
    new_fieldnames.append(field)

    if field == "Invoice No":
        new_fieldnames.append("Date")

# Ask for dates
for row in rows:
    invoice = row["Invoice No"]

    print("\nInvoice:", invoice)
    date = input("Enter transaction date (YYYY-MM-DD): ")

    row["Date"] = date

# Save updated file
with open(file_name, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=new_fieldnames)
    writer.writeheader()

    for row in rows:
        writer.writerow(row)

print("\n===================================")
print("Dates added successfully!")
print("AI_Accounting_Report.csv updated.")
print("===================================")
