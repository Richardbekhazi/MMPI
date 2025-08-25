import pandas as pd
import json
import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox
import xlwings as xw

# Paths
json_folder = r'C:\Users\Richa\OneDrive\Desktop\MMPI Final Project\MMPI_JSON'
output_folder = r'C:\Users\Richa\OneDrive\Desktop\MMPI 2025'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get JSON file names without extension
json_files = sorted([f[:-5] for f in os.listdir(json_folder) if f.endswith('.json')])

# Function to create main Excel file
def json_to_excel(json_data, output_excel_file):
    questions = json_data["questions"]
    max_question_number = max(item["English Question Number"] for item in questions)

    df = pd.DataFrame(index=range(1, max_question_number + 1),
                      columns=["English Question Number", "Arabic Question Number", "Y", "Question Text", "Answer"])

    for item in questions:
        qn = item["English Question Number"]
        df.loc[qn] = [
            item["English Question Number"],
            item["Arabic Question Number"],
            item["Y"],
            item["Question Text"],
            item["Answer"]
        ]

    df.to_excel(output_excel_file, index=False)

# Function to copy the MMPI template file based on gender
def copy_mmpi_template(gender, person_name):
    template_file = "Male MMPI.xlsx" if gender.lower() == "male" else "Female MMPI.xlsx"
    template_path = os.path.join(output_folder, template_file)

    if not os.path.exists(template_path):
        messagebox.showerror("Template Missing", f"Template file not found: {template_path}")
        return

    output_copy_path = os.path.join(output_folder, f"{person_name} MMPI.xlsx")
    shutil.copyfile(template_path, output_copy_path)

# Convert on button click
def convert_selected_file():
    selected_name = combo.get()
    if selected_name not in json_files:
        messagebox.showwarning("Invalid Selection", "Please select a valid name from the list.")
        return

    input_json_file = os.path.join(json_folder, selected_name + '.json')
    output_excel_file = os.path.join(output_folder, selected_name + '.xlsx')

    try:
        with open(input_json_file, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        # Save primary Excel file
        json_to_excel(json_data, output_excel_file)

        # Extract gender and name
        gender = json_data["user_info"]["gender"]
        person_name = json_data["user_info"]["name"]

        # Copy the MMPI template
        copy_mmpi_template(gender, person_name)

        # Construct path for copied MMPI file
        mmpi_file_path = os.path.join(output_folder, f"{person_name} MMPI.xlsx")

        # ✅ First update the chart info box in the MMPI Excel
        update_excel_chart_info(mmpi_file_path, json_data["user_info"])

        # ✅ Then open the files for the user to view
        os.startfile(output_excel_file)
        os.startfile(mmpi_file_path)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_excel_chart_info(excel_path, user_info):
    import xlwings as xw

    name = user_info["name"]
    age = user_info["age"]
    case_number = user_info["folder_number"]
    date = user_info["date"]

    try:
        # Build multi-line title with tabs (as shown)
        chart_title = (
            f"Name:\t\t {name}\n"
            f"Case Number:\t {case_number}\n"
            f"Date:\t\t {date}\n"
            f"Age:\t\t {age} Years"
        )

        app = xw.App(visible=False)
        wb = app.books.open(excel_path)

        # ✅ Write to AC1 in the "Tables" sheet
        sheet = wb.sheets["Tables"]
        sheet.range("AC1").value = chart_title

        wb.save()
        wb.close()
        app.quit()

    except Exception as e:
        messagebox.showerror("Excel Update Error", f"Failed to update chart info in AC1:\n{e}")



# Search filter for combobox
def on_keyrelease(event):
    value = event.widget.get().lower()
    filtered = [name for name in json_files if value in name.lower()]
    combo['values'] = filtered

# UI Setup
root = tk.Tk()
root.title("MMPI JSON to Excel Converter")
root.geometry("500x180")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 11))
style.configure("TCombobox", font=("Segoe UI", 11))

# Widgets
ttk.Label(root, text="Select a name to convert to Excel:").pack(pady=(15, 5))

combo = ttk.Combobox(root, values=json_files, width=50)
combo.pack(pady=5)
combo.bind('<KeyRelease>', on_keyrelease)

ttk.Button(root, text="Convert to Excel", command=convert_selected_file).pack(pady=15)

root.mainloop()
