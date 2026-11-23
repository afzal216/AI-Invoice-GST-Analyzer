import csv
import os
import shutil
import subprocess
import sys

def run_analysis_and_prediction():

    print("\n===================================")
    print("   RUNNING AI ANALYSIS")
    print("===================================")

    subprocess.run(
        [sys.executable, "AI_Financial_Analysis.py"]
    )

    print("\n===================================")
    print("   RUNNING AI PREDICTION")
    print("===================================")

    subprocess.run(
        [sys.executable, "AI_Financial_Prediction.py"]
    )

    print("\nAI Analysis and Prediction completed successfully!")

    show_prediction_result()


def show_prediction_result():

    file_name = "AI_Financial_Prediction_Report.csv"

    if not os.path.exists(file_name):
        print("\nPrediction report not found.")
        return

    with open(file_name, "r", newline="") as file:

        reader = csv.DictReader(file)
        rows = list(reader)

    if len(rows) == 0:
        print("\nPrediction report is empty.")
        return

    result = rows[-1]

    print("\n===================================")
    print("       AI PREDICTION RESULT")
    print("===================================")

    print("Financial Trend       :", result["Financial Trend"])
    print("Financial Health Score:", result["Financial Health Score"])
    print("Financial Health      :", result["Financial Health Status"])
    print("Predicted Next Date   :", result["Predicted Next Date"])
    print("Predicted Next Amount :", result["Predicted Next Amount"])
    print("AI Recommendation     :", result["AI Recommendation"])

    print("===================================")

def create_backup():

    file_name = "AI_Accounting_Report.csv"
    backup_name = "AI_Accounting_Report_backup.csv"

    if os.path.exists(file_name):

        shutil.copy2(file_name, backup_name)

        print("\nBackup created successfully!")

print("===================================")
print("   AI INVOICE & GST ANALYZER")
print("===================================")

while True:

    print("\n1. Add New Transaction")
    print("2. Edit Existing Transaction")
    print("3. Delete Existing Transaction")
    print("4. View All Invoice")
    print("5. Search Invoice")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # EXIT
    if choice == "6":
        print("\nThank you for using AI Accounting System!")
        break

    # INVALID CHOICE
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Please select 1 to 6")
        continue

# ==========================================
    # EDIT EXISTING TRANSACTION
    # ==========================================

    if choice == "2":

        file_name = "AI_Accounting_Report.csv"

        if not os.path.exists(file_name):
            print("\nNo accounting data found.")
            continue

        invoice_to_edit = input(
            "\nEnter invoice number to edit (or B to go back): "
        ).strip()

        if invoice_to_edit.upper() == "B":
            print("\nReturning to main menu...")
            continue

        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            rows = list(reader)

        if not fieldnames or not rows:
            print("\nNo invoices found.")
            continue

        invoice_index = None

        for index, row in enumerate(rows):
            if row["Invoice No"].strip().upper() == invoice_to_edit.upper():
                invoice_index = index
                break

        if invoice_index is None:
            print("\nInvoice not found.")
            continue

        row = rows[invoice_index]

        print("\n========== INVOICE FOUND ==========")
        print("Invoice No  :", row["Invoice No"])
        print("Customer    :", row["Customer"])
        print("Description :", row["Description"])
        print("Category    :", row["Category"])
        print("Taxable Amt :", row["Taxable Amount"])
        print("GST Rate    :", row["GST Rate"])
        print("===================================")

        original_row = row.copy()
        cancelled = False

        while True:

            print("\n========== EDIT MENU ==========")
            print("1. Edit Invoice Number")
            print("2. Edit Customer Name")
            print("3. Edit Description")
            print("4. Edit Taxable Amount")
            print("5. Edit GST Rate")
            print("6. Save Changes")
            print("7. Cancel Editing")
            print("===============================")

            edit_choice = input("Enter your choice: ").strip()

            if edit_choice == "7":
                rows[invoice_index] = original_row
                cancelled = True
                print("\nEditing cancelled.")
                break

            elif edit_choice == "1":

                new_invoice_no = input(
                    "Enter new invoice number: "
                ).strip()

                if not new_invoice_no:
                    print("\nInvoice number cannot be empty.")
                    continue

                duplicate = any(
                    other_row["Invoice No"].strip().upper()
                    == new_invoice_no.upper()
                    for index, other_row in enumerate(rows)
                    if index != invoice_index
                )

                if duplicate:
                    print("\nThat invoice number already exists!")
                else:
                    row["Invoice No"] = new_invoice_no
                    print("\nInvoice number updated.")

            elif edit_choice == "2":

                new_customer = input(
                    "Enter new customer name: "
                ).strip()

                if new_customer:
                    row["Customer"] = new_customer
                    print("\nCustomer name updated.")
                else:
                    print("\nCustomer name cannot be empty.")

            elif edit_choice == "3":

                new_description = input(
                    "Enter new description: "
                ).strip()

                if new_description:
                    row["Description"] = new_description

                    description_lower = new_description.lower()

                    if (
                        "laptop" in description_lower
                        or "computer" in description_lower
                    ):
                        row["Category"] = "Office Equipment"

                    elif "rent" in description_lower:
                        row["Category"] = "Rent Expense"

                    elif (
                        "electricity" in description_lower
                        or "electric" in description_lower
                    ):
                        row["Category"] = "Utilities"

                    elif (
                        "salary" in description_lower
                        or "wages" in description_lower
                    ):
                        row["Category"] = "Salary Expense"

                    elif (
                        "sale" in description_lower
                        or "sales" in description_lower
                    ):
                        row["Category"] = "Sales"

                    elif "purchase" in description_lower:
                        row["Category"] = "Purchase"

                    else:
                        row["Category"] = "Other Expense"

                    print("\nDescription and category updated.")

                else:
                    print("\nDescription cannot be empty.")

            elif edit_choice == "4":

                try:
                    new_amount = float(
                        input("Enter new taxable amount: ")
                    )

                    if new_amount < 0:
                        print("\nAmount cannot be negative.")
                        continue

                    row["Taxable Amount"] = new_amount
                    print("\nTaxable amount updated.")

                except ValueError:
                    print("\nPlease enter a valid number.")

            elif edit_choice == "5":

                try:
                    new_gst_rate = float(
                        input("Enter new GST rate (%): ")
                    )

                    if not 0 <= new_gst_rate <= 100:
                        print("\nGST rate must be between 0 and 100.")
                        continue

                    row["GST Rate"] = new_gst_rate
                    print("\nGST rate updated.")

                except ValueError:
                    print("\nPlease enter a valid number.")

            elif edit_choice == "6":
                break

            else:
                print("\nInvalid choice. Select 1 to 7.")

        if cancelled:
            continue

        # Recalculate GST and total amount
        try:
            amount = float(row["Taxable Amount"])
            gst_rate = float(row["GST Rate"])

            gst_amount = amount * gst_rate / 100
            cgst = gst_amount / 2
            sgst = gst_amount / 2
            total_amount = amount + gst_amount

            row["CGST"] = round(cgst, 2)
            row["SGST"] = round(sgst, 2)
            row["Total GST"] = round(gst_amount, 2)
            row["Total Amount"] = round(total_amount, 2)

        except (ValueError, KeyError):
            print("\nCould not calculate GST. Changes were not saved.")
            rows[invoice_index] = original_row
            continue

        # Create backup before saving changes
        create_backup()

        with open(file_name, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(rows)

        print("\nInvoice updated successfully!")
        print("Invoice No  :", row["Invoice No"])
        print("Customer    :", row["Customer"])
        print("Description :", row["Description"])
        print("Taxable Amt :", row["Taxable Amount"])
        print("GST Rate    :", row["GST Rate"])
        print("Total GST   :", row["Total GST"])
        print("Total Amount:", row["Total Amount"])

        continue
    # ==========================================
    # VIEW ALL INVOICES
    # ==========================================

    if choice == "4":

        file_name = "AI_Accounting_Report.csv"

        if not os.path.exists(file_name):
            print("\nNo accounting data found.")
            continue

        with open(file_name, "r", newline="") as file:

            reader = csv.DictReader(file)
            rows = list(reader)

        if len(rows) == 0:
            print("\nNo invoices found.")

        else:
            print("\n========== ALL INVOICES ==========")

            print(
                f"{'Invoice No':<12}"
                f"{'Date':<13}"
                f"{'Customer':<20}"
                f"{'Total Amount':>15}"
            )

            print("-" * 60)

            for row in rows:

                print(
                    f"{row['Invoice No']:<12}"
                    f"{row['Date']:<13}"
                    f"{row['Customer']:<20}"
                    f"{row['Total Amount']:>15}"
                )

            print("-" * 60)
            print("Total Invoices:", len(rows))

            print("==================================")

        continue
    
    # ==========================================
    # DELETE EXISTING TRANSACTION
    # ==========================================

    if choice == "3":

        file_name = "AI_Accounting_Report.csv"

        if not os.path.exists(file_name):
            print("\nNo accounting data found.")
            continue

        invoice_to_delete = input(
            "\nEnter invoice number to delete (or B to go back): "
            )
        if invoice_to_delete.strip().upper() == "B":
            print("\nReturning to main menu...")
            continue

        rows = []
        invoice_found = False
        confirm = "no"

        with open(file_name, "r", newline="") as file:

            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames

            for row in reader:

                if row["Invoice No"].strip().upper() == invoice_to_delete.strip().upper():

                    invoice_found = True

                    print("\nInvoice found!")
                    print("-----------------------------------")
                    print("Invoice No  :", row["Invoice No"])
                    print("Customer    :", row["Customer"])
                    print("Description :", row["Description"])
                    print("Category    :", row["Category"])
                    print("Total Amount:", row["Total Amount"])
                    print("-----------------------------------")

                    confirm = input(
                        "Are you sure you want to delete this invoice? (yes/no): "
                    )

                    if confirm.lower() != "yes":
                        rows.append(row)

                else:

                    rows.append(row)

        if not invoice_found:

            print("\nInvoice not found.")

        elif confirm.lower() == "yes":

            create_backup()

            with open(file_name, "w", newline="") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(rows)

            print("\nInvoice deleted successfully!")

        else:

            print("\nDeletion cancelled.")

        continue
    # ==========================================
    # SEARCH INVOICE
    # ==========================================

    if choice == "5":

        file_name = "AI_Accounting_Report.csv"

        if not os.path.exists(file_name):
            print("\nNo accounting data found.")
            continue

        invoice_to_search = input(
            "\nEnter invoice number to search (or B to go back): "
            )
        if invoice_to_search.strip().upper() == "B":
            print("\nReturning to main menu...")
            continue

        invoice_found = False

        with open(file_name, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["Invoice No"].strip().upper() == invoice_to_search.strip().upper():

                    invoice_found = True

                    print("\n========== INVOICE FOUND ==========")

                    print("Invoice No  :", row["Invoice No"])
                    print("Date        :", row["Date"])
                    print("Customer    :", row["Customer"])
                    print("Description :", row["Description"])
                    print("Category    :", row["Category"])
                    print("Taxable Amt :", row["Taxable Amount"])
                    print("GST Rate    :", row["GST Rate"])
                    print("CGST        :", row["CGST"])
                    print("SGST        :", row["SGST"])
                    print("Total GST   :", row["Total GST"])
                    print("Total Amount:", row["Total Amount"])

                    print("===================================")

                    break

        if not invoice_found:
            print("\nInvoice not found.")

        continue

    # ==========================================
    # ADD NEW TRANSACTION
    # ==========================================

    if choice == "1":

        file_name = "AI_Accounting_Report.csv"

        go_back = False

        while True:

            invoice_no = input(
                "\nEnter invoice number (or B to go back): "
            )

            if invoice_no.strip().upper() == "B":
                print("\nReturning to main menu...")
                go_back = True
                break

            invoice_exists = False

            if os.path.exists(file_name):

                with open(file_name, "r", newline="") as file:

                    reader = csv.DictReader(file)

                    for row in reader:

                        if row["Invoice No"].strip().upper() == invoice_no.strip().upper():

                            invoice_exists = True
                            break

            if invoice_exists:

                print("\nInvoice number", invoice_no, "already exists!")
                print("Please enter a different invoice number.")

            else:

                break

        if go_back:
            continue

        date = input("Enter transaction date (YYYY-MM-DD): ")
        customer = input("Enter customer name: ")
        description = input("Enter transaction description: ")

        amount = float(input("Enter taxable amount: "))
        gst_rate = float(input("Enter GST rate (%): "))

        # AI-style transaction classification
        description_lower = description.lower()

        if "laptop" in description_lower or "computer" in description_lower:
            category = "Office Equipment"

        elif "rent" in description_lower:
            category = "Rent Expense"

        elif "electricity" in description_lower or "electric" in description_lower:
            category = "Utilities"

        elif "salary" in description_lower or "wages" in description_lower:
            category = "Salary Expense"

        elif "sale" in description_lower or "sales" in description_lower:
            category = "Sales"

        elif "purchase" in description_lower:
            category = "Purchase"

        else:
            category = "Other Expense"

        # GST calculation
        gst_amount = amount * gst_rate / 100

        cgst = gst_amount / 2
        sgst = gst_amount / 2

        total_amount = amount + gst_amount

        # Display result
        print("\n========== ACCOUNTING RESULT ==========")

        print("Invoice No  :", invoice_no)
        print("Customer    :", customer)
        print("Description :", description)
        print("Category    :", category)
        print("Taxable Amt :", amount)
        print("GST Rate    :", gst_rate, "%")
        print("CGST        :", cgst)
        print("SGST        :", sgst)
        print("Total GST   :", gst_amount)
        print("Total Amount:", total_amount)

        print("=======================================")

        # Save to CSV
        file_exists = os.path.exists(file_name)

        with open(file_name, "a", newline="") as file:

            writer = csv.writer(file)

            if not file_exists:

                writer.writerow([
                    "Invoice No",
                    "Date",
                    "Customer",
                    "Description",
                    "Category",
                    "Taxable Amount",
                    "GST Rate",
                    "CGST",
                    "SGST",
                    "Total GST",
                    "Total Amount"
                ])

            writer.writerow([
                invoice_no,
                date,
                customer,
                description,
                category,
                amount,
                gst_rate,
                cgst,
                sgst,
                gst_amount,
                total_amount
            ])

        print("\nTransaction saved successfully!")

        run_analysis_and_prediction()

        continue
