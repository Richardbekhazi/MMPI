import json
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import tksheet
from indices_config import indices_F, indices_K_positive, indices_K_negative, indices_Hs, indices_D_positive, indices_D_negative
from indices_config import indices_Hy_positive, indices_Hy_negative , indices_Pd_positive, indices_Pd_negative, indices_Mf_positive, indices_Mf_negative
from indices_config import indices_Pa_positive, indices_Pa_negative, indices_Pt_positive, indices_Pt_negative
from indices_config import indices_Sc_positive, indices_Sc_negative, indices_Ma_positive, indices_Ma_negative
from indices_config import indices_Si_positive, indices_Si_negative, indices_Mf_gender
from decimal import Decimal, ROUND_HALF_EVEN

# Variable index mapping
variable_indices = {
    'K': indices_K_positive + indices_K_negative,
    'F': indices_F,
    'Hs': indices_Hs,
    'D': indices_D_positive + indices_D_negative,
    'Hy': indices_Hy_positive + indices_Hy_negative,
    'Pd': indices_Pd_positive + indices_Pd_negative,
    'Mf': indices_Mf_positive + indices_Mf_negative,
    'Pa': indices_Pa_positive + indices_Pa_negative,
    'Pt': indices_Pt_positive + indices_Pt_negative,
    'Sc': indices_Sc_positive + indices_Sc_negative,
    'Ma': indices_Ma_positive + indices_Ma_negative,
    'Si': indices_Si_positive + indices_Si_negative,
    'Mf_Gender': indices_Mf_gender
    # Add other variables if needed
}

def build_mapping(formula_matrix, columns):
    mapping = {}
    for row_index, row in enumerate(formula_matrix):
        Y = row_index + 1  # Rows correspond to Y values starting from 1
        for col_index, cell in enumerate(row):
            if col_index >= len(columns):
                continue  # Skip columns beyond the columns list
            Arabic_Letter = columns[col_index]
            if cell:
                # cell is something like '=C1' or '=E2'
                if cell.startswith('=C'):
                    symbol = 'C'
                elif cell.startswith('=E'):
                    symbol = 'E'
                else:
                    continue  # skip if it's not '=C...' or '=E...'
                mapping[(Y, Arabic_Letter)] = symbol
            else:
                # Empty cell
                mapping[(Y, Arabic_Letter)] = None
    return mapping

def advanced_analysis(user_data):
    # Define the columns (Arabic letters)
    columns = ['أ', 'ب', 'ج', 'ح', 'د', 'ز', 'ط', 'ه', 'و', 'ي']  # Adjust as per your matrix

    # Include your actual formula_matrix here
    formula_matrix = [
        ['=C1', '=E2', '', '', '=C3', '=E4', '=E5', '=E6', '=E7', '=E8'],
        ['=C10', '=E11', '', '=E12', '=E13', '', '=E14', '', '=C15', ''],
        ['=E17', '=E18', '=E19', '=E20', '', '=E21', '=E22', '=C23', '=E24', ''],
        ['=C26', '=E27', '', '=E28', '', '=E29', '=E30', '', '=E31', '=E32'],
        ['=C34', '', '=E35', '', '=C36', '', '', '', '=E37', '=C38'],
        ['=C40', '=C41', '=E42', '=E43', '=C44', '=E45', '=E46', '', '=C47', '=E48'],
        ['', '=E50', '=C51', '=E52', '=C53', '=E54', '=E55', '=E56', '=C57', '=E58'],
        ['=C60', '=C61', '=E62', '=E63', '=E64', '', '=E65', '', '=E66', ''],
        ['=E68', '=C69', '=E70', '=C71', '', '=E72', '=C73', '=E74', '=E75', ''],
        ['=C77', '=C78', '=E79', '=E80', '=C81', '=E82', '', '=E83', '=E84', '=E85'],
        ['=E87', '=E88', '=E89', '=E90', '=C91', '=E92', '', '=E93', '', '=E94'],
        ['=E96', '=C97', '=E98', '=E99', '', '=C100', '=E101', '=C102', '', '=E103'],
        ['=E105', '=E106', '=C107', '=E108', '', '=E109', '=E110', '', '', '=E111'],
        ['=E113', '', '=C114', '=E115', '', '', '', '', '=E116', ''],
        ['=E118', '=E119', '=C120', '=E121', '=C122', '', '=E123', '=E124', '=C125', ''],
        ['=C127', '=E128', '=C129', '=E130', '=C131', '=C132', '', '=C133', '', ''],
        ['=C135', '=E136', '=C137', '=E138', '=C139', '', '', '=C140', '=E141', '=C142'],
        ['=C144', '=C145', '=E146', '=E147', '=C148', '=C149', '', '=C150', '=E151', '=E152'],
        ['=E154', '=E155', '', '=E156', '=C157', '=E158', '', '', '', '=E159'],
        ['=E161', '=C162', '=E163', '=E164', '', '=E165', '', '=C166', '=C167', '=E168'],
        ['=E170', '', '', '=E171', '=E172', '=E173', '=E174', '=E175', '', ''],
        ['=E177', '=C178', '=E179', '=E180', '=E181', '=E182', '=C183', '=E184', '=E185', ''],
        ['=C187', '', '', '', '=E188', '=C189', '=E190', '=E191', '', '=E192'],
        ['=C194', '', '=E195', '=E196', '=E197', '=E198', '', '=E199', '', '=E200'],
        ['=E202', '=C203', '=E204', '=E205', '=E206', '=E207', '=E208', '', '=E209', '=E210'],
        ['=E212', '', '', '=E213', '=E214', '=E215', '=E216', '=E217', '', '=E218'],
        ['=C220', '=C221', '=E222', '=C223', '', '', '=E224', '=E225', '', ''],
        ['', '=E227', '=C228', '=E229', '', '', '=C230', '=C231', '', '=C232'],
        ['', '=C234', '=C235', '=E236', '=E237', '=E238', '=E239', '=C240', '', '=E241'],
        ['=E243', '=C244', '', '=E245', '=E246', '=C247', '=E248', '=E249', '=E250', ''],
        ['=C252', '=E254', '=E254', '=C255', '', '=E256', '=E257', '=E258', '=E259', '=C260'],
        ['=C262', '=E263', '', '=E264', '=E265', '=E266', '=E267', '=C268', '', '=E269'],
        ['', '=E271', '=E272', '=C273', '=E274', '=E275', '=E276', '=C277', '=E278', '=C279'],
        ['', '', '', '', '=E281', '=E282', '=E283', '=C284', '=E285', '=E286'],
        ['=C288', '=E289', '=C290', '', '=C291', '=E292', '=E293', '=C294', '=E295', ''],
        ['=C297', '=E298', '=E299', '=C300', '=E301', '=E302', '=E303', '=C304', '=E305', ''],
        ['=C307', '=E308', '', '=E309', '=E310', '=E311', '=E312', '=E313', '=C314', ''],
        ['=E316', '=E317', '', '=E318', '=C319', '=C320', '=E321', '=C322', '=C323', ''],
        ['', '', '', '', '=C325', '', '=E326', '=C327', '=C328', '=E329'],
        ['=E331', '=E332', '', '', '', '=E333', '=C334', '=C335', '', '=E336'],
        ['=C338', '', '=C339', '', '=E340', '=E341', '=E342', '=C343', '=E344', '=C345'],
        ['=C347', '=E348', '=E349', '=E350', '=C351', '=E352', '', '=E353', '=E354', '=C355'],
        ['=C357', '', '=C358', '=C359', '=E360', '=E361', '', '=E362', '=E363', '=C364'],
        ['=C366', '', '', '', '=C367', '=E368', '=E369', '=E370', '=E371', '=C372'],
        ['=E374', '', '=C375', '', '=C376', '=E377', '=E378', '', '=E379', '=C380'],
        ['=C382', '=C384', '=E384', '', '=E385', '', '', '=C386', '=E387', '=C388'],
        ['=E390', '=E391', '=C392', '=E393', '=E394', '=E395', '', '=C396', '', '=C397'],
        ['=E399', '=C400', '=E401', '', '=C402', '=E403', '', '=E404', '', '=C405'],
        ['=E407', '=E408', '=C409', '=E410', '=E411', '=C412', '=E413', '=C414', '=E415', '=C416'],
        ['=C418', '=E419', '=E420', '=E421', '=E422', '=E423', '=C424', '=E425', '=E426', '=C427'],
        ['=C429', '=C430', '=E431', '=E432', '=E433', '=E434', '=E435', '=C436', '=E437', '=C438'],
        ['=C440', '=E441', '=E442', '=C443', '=E444', '=C445', '', '=E446', '=C447', '=C448'],
        ['=E450', '=E451', '=E452', '=E453', '=E454', '=E455', '=E456', '=E457', '', '=C458'],
        ['=E460', '=C461', '', '=C462', '=E463', '=E464', '=E465', '=C466', '', '=C467'],
        ['=C469', '=C470', '=E471', '=E472', '=E473', '=E474', '', '=C475', '', '=C476']
    ]

    # Build the mapping from formula_matrix
    mapping = build_mapping(formula_matrix, columns)

    # Determine the maximum Y value to size the result_matrix
    max_Y = max(q['Y'] for q in user_data)
    result_matrix = [[None for _ in columns] for _ in range(max_Y)]

    # Process each question in the user data
    for q in user_data:
        Y = q['Y']
        Arabic_Letter = q['Arabic Question Number']
        mapping_key = (Y, Arabic_Letter)
        symbol = mapping.get(mapping_key)

        if symbol:
            answer = q.get('Answer')
            # Determine the cell value based on the symbol and the user's answer
            if symbol == 'C':
                value = 1 if answer == 'No' else 0
            elif symbol == 'E':
                value = 1 if answer == 'Yes' else 0
            else:
                value = 0

            # Place the value in the result_matrix
            row_index = Y - 1  # Zero-based index
            if Arabic_Letter in columns:
                col_index = columns.index(Arabic_Letter)
                result_matrix[row_index][col_index] = value
        else:
            # Cell is empty in the matrix; skip
            pass

    return result_matrix, columns


def highlight_cells(variable_name, sheet, result_matrix, columns):
    """Function to highlight cells."""
    # Clear existing highlights
    sheet.highlight_cells(row=None, column=None, bg='white', fg='black')  # Reset all cells

    if variable_name == 'L':
        # Dynamically highlight L (Rows 41 to 55 and column 'ي', i.e., index 9)
        col_index = columns.index('ي')  # Find index for column 'ي'
        for row_index in range(41, 56):  # Highlight rows 42 to 56 (0-indexed)
            if row_index < len(result_matrix):
                sheet.highlight_cells(row=row_index, column=col_index + 1, bg='yellow', fg='black')
    else:
        # Use pre-defined indices for K and F
        indices_to_highlight = variable_indices.get(variable_name, [])
        for row_index, col_index in indices_to_highlight:
            adjusted_col_index = col_index + 1
            sheet.highlight_cells(row=row_index, column=adjusted_col_index, bg='yellow', fg='black')

def reset_highlights(sheet):
    """Reset all highlighted cells to their default state (white background)."""
    total_rows = sheet.get_total_rows()  # Get the total number of rows
    total_cols = sheet.get_total_columns()  # Get the total number of columns

    # Loop through every cell in the table and set its background color to white
    for row_index in range(total_rows):
        for col_index in range(total_cols):
            sheet.highlight_cells(row=row_index, column=col_index, bg='white', fg='black')



def display_analysis(result_matrix, columns, user_info):
    root = tk.Tk()
    root.title(f"نتائج التحليل المتقدم - {user_info.get('name', '')}")

    # Create the sheet
    sheet = tksheet.Sheet(root)
    sheet.pack(fill=tk.BOTH, expand=True)

    # Prepare data for the sheet
    data = []
    for row_index, row in enumerate(result_matrix):
        row_values = [row_index + 1] + [cell if cell is not None else '' for cell in row]
        data.append(row_values)

    # Set headers
    headers = ['Y'] + columns

    # Set data and headers to the sheet
    sheet.headers(headers)
    sheet.set_sheet_data(data)

    # Create buttons to highlight variables and reset
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    highlight_k_button = tk.Button(button_frame, text="إبراز K", command=lambda: highlight_cells('K', sheet, result_matrix, columns))
    highlight_k_button.pack(side=tk.LEFT, padx=5)

    highlight_l_button = tk.Button(button_frame, text="إبراز L", command=lambda: highlight_cells('L', sheet, result_matrix, columns))
    highlight_l_button.pack(side=tk.LEFT, padx=5)

    highlight_f_button = tk.Button(button_frame, text="إبراز F", command=lambda: highlight_cells('F', sheet, result_matrix, columns))
    highlight_f_button.pack(side=tk.LEFT, padx=5)

    highlight_hs_button = tk.Button(button_frame, text="إبراز Hs", command=lambda: highlight_cells('Hs', sheet, result_matrix, columns))
    highlight_hs_button.pack(side=tk.LEFT, padx=5)

    highlight_d_button = tk.Button(button_frame, text="إبراز D", command=lambda: highlight_cells('D', sheet, result_matrix, columns))
    highlight_d_button.pack(side=tk.LEFT, padx=5)

    highlight_hy_button = tk.Button(button_frame, text="إبراز Hy", command=lambda: highlight_cells('Hy', sheet, result_matrix, columns))
    highlight_hy_button.pack(side=tk.LEFT, padx=5)

    highlight_pd_button = tk.Button(button_frame, text="إبراز Pd", command=lambda: highlight_cells('Pd', sheet, result_matrix, columns))
    highlight_pd_button.pack(side=tk.LEFT, padx=5)

    highlight_mf_button = tk.Button(button_frame, text="إبراز Mf", command=lambda: highlight_cells('Mf', sheet, result_matrix, columns))
    highlight_mf_button.pack(side=tk.LEFT, padx=5)

    highlight_pa_button = tk.Button(button_frame, text="إبراز Pa", command=lambda: highlight_cells('Pa', sheet, result_matrix, columns))
    highlight_pa_button.pack(side=tk.LEFT, padx=5)

    highlight_pt_button = tk.Button(button_frame, text="إبراز Pt", command=lambda: highlight_cells('Pt', sheet, result_matrix, columns))
    highlight_pt_button.pack(side=tk.LEFT, padx=5)

    highlight_sc_button = tk.Button(button_frame, text="إبراز Sc", command=lambda: highlight_cells('Sc', sheet, result_matrix, columns))
    highlight_sc_button.pack(side=tk.LEFT, padx=5)

    highlight_ma_button = tk.Button(button_frame, text="إبراز Ma", command=lambda: highlight_cells('Ma', sheet, result_matrix, columns))
    highlight_ma_button.pack(side=tk.LEFT, padx=5)

    highlight_si_button = tk.Button(button_frame, text="إبراز Si", command=lambda: highlight_cells('Si', sheet, result_matrix, columns))
    highlight_si_button.pack(side=tk.LEFT, padx=5)

    highlight_gender_button = tk.Button(button_frame, text="إبراز Mf Gender", command=lambda: highlight_cells('Mf_Gender', sheet, result_matrix, columns))
    highlight_gender_button.pack(side=tk.LEFT, padx=5)


    reset_button = tk.Button(button_frame, text="إعادة ضبط الإبراز", command=lambda: reset_highlights(sheet))
    reset_button.pack(side=tk.LEFT, padx=5)

    root.mainloop()


def display_table(user_json_file_name):
    # Load the JSON file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    user_json_path = os.path.join(script_dir, 'MMPI_JSON', user_json_file_name)
    
    with open(user_json_path, 'r', encoding='utf-8') as f:
        user_file_data = json.load(f)
        # Handle both old and new formats
        if isinstance(user_file_data, list):
            # Old format: user_file_data is a list of questions
            user_data = user_file_data
            user_info = {}  # No user info available
            # Update user_file_data to new format
            user_file_data = {
                "user_info": user_info,
                "questions": user_data
            }
        else:
            # New format: user_file_data is a dictionary
            user_info = user_file_data['user_info']
            user_data = user_file_data['questions']

    # Create the root window with adjusted dimensions
    root = tk.Tk()
    root.title(f"جدول الإجابات - {user_info.get('name', '')}")
    root.geometry("900x600")  # Set the window size (width x height)

    # Configure the window for RTL layout
    root.option_add("*TLabel.Direction", "rtl")
    root.option_add("*TButton.Direction", "rtl")
    root.option_add("*TEntry.Direction", "rtl")

    # Create a frame to hold the user info
    user_info_frame = tk.Frame(root)
    user_info_frame.pack(pady=10)

    # Map English gender to Arabic
    gender_reverse_map = {'Male': 'ذكر', 'Female': 'أنثى', 'Other': 'آخر'}

    # Display user info labels
    name_label = tk.Label(user_info_frame, text=f"Name: {user_info.get('name', '')}", font=('Helvetica', 12))
    name_label.pack(side=tk.LEFT, padx=5)

    age_label = tk.Label(user_info_frame, text=f"Age: {user_info.get('age', '')}", font=('Helvetica', 12))
    age_label.pack(side=tk.LEFT, padx=5)

    date_label = tk.Label(user_info_frame, text=f"Date: {user_info.get('date', '')}", font=('Helvetica', 12))
    date_label.pack(side=tk.LEFT, padx=5)

    # Use the mapped gender for display
    displayed_gender = gender_reverse_map.get(user_info.get('gender', 'Other'), 'آخر')
    gender_label = tk.Label(user_info_frame, text=f"Gender: {displayed_gender}", font=('Helvetica', 12))
    gender_label.pack(side=tk.LEFT, padx=5)

    # Create a table using Treeview with RTL support and Arabic column names
    table = ttk.Treeview(root, columns=('Answer', 'Question', 'Q_Number'), show='headings')

    # Set the column headers in Arabic and align them
    table.heading('Answer', text='الإجابة', anchor='e')  # Align answers to the right
    table.heading('Question', text='نص السؤال', anchor='e')  # Right-align the question text
    table.heading('Q_Number', text='رقم السؤال', anchor='w')  # Align question number to the left

    # Configure the column widths
    table.column('Answer', width=80, anchor='e')  # Adjust the width for the answer
    table.column('Question', width=550, anchor='e')  # Adjust the width for the question text
    table.column('Q_Number', width=100, anchor='w')  # Adjust the width for the question number

    # Populate the table with user data, combining Arabic Question Number and Y as the Question Number
    for q in user_data:
        question_number = f"{q['Y']}{q['Arabic Question Number']}"  # Combine Y and Arabic Letter
        answer = q.get('Answer', 'None')  # Ensure we handle cases where 'Answer' might be missing
        table.insert('', 'end', values=(answer, q['Question Text'], question_number))

    table.pack(fill=tk.BOTH, expand=True)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    # Button to show the answer distribution graph
    show_graph_button = tk.Button(button_frame, text="عرض رسم توزيع الإجابات", command=lambda: show_graph(user_data, user_info))
    show_graph_button.pack(side=tk.LEFT, padx=5)

    # Button to perform the advanced analysis
    advanced_analysis_button = tk.Button(button_frame, text="تحليل متقدم", command=lambda: perform_advanced_analysis(user_data, user_info))
    advanced_analysis_button.pack(side=tk.LEFT, padx=5)

    # Button to display original values
    brut_button = tk.Button(button_frame, text="عرض القيم الأولية", command=lambda: display_brut_values(user_data, user_info))
    brut_button.pack(side=tk.LEFT, padx=5)

    # Button to display final values
    final_button = tk.Button(button_frame, text="عرض القيم النهائية", command=lambda: display_final_values(user_data, user_info))
    final_button.pack(side=tk.LEFT, padx=5)

    root.mainloop()

def compute_variables(result_matrix, columns, user_info):
    variables = {}
    
    # Variable L
    try:
        col_index = columns.index('ي')  # Column 'ي' corresponds to 'T' in your formula
    except ValueError:
        messagebox.showerror("Error", "Column 'ي' not found in the matrix.")
        return
    
    L_value = 0
    for row_index in range(41, 56):  # Rows 42 to 56 (indices 41 to 55)
        if row_index < len(result_matrix):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                L_value += cell_value
    variables['L'] = L_value
    
    # Variable F
    F_value = 0
    for row_index, col_index in indices_F:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                F_value += cell_value
    variables['F'] = F_value
    
    # Variable K
    positive_sum = 0
    for row_index, col_index in indices_K_positive:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                positive_sum += cell_value
    
    negative_sum = 0
    for row_index, col_index in indices_K_negative:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                negative_sum += cell_value
    
    K_value = 20 + positive_sum - negative_sum
    variables['K'] = K_value
    
    # Variable Hs (new addition)
    Hs_value = 0
    for row_index, col_index in indices_Hs:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Hs_value += cell_value
    variables['Hs'] = Hs_value

    # Variable D
    D_positive_sum = 0
    for row_index, col_index in indices_D_positive:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                D_positive_sum += cell_value
    
    D_negative_sum = 0
    for row_index, col_index in indices_D_negative:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                D_negative_sum += cell_value
    
    D_value = 16 + D_positive_sum - D_negative_sum
    variables['D'] = D_value

    # Variable Hy
    Hy_positive_sum = 0
    for row_index, col_index in indices_Hy_positive:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Hy_positive_sum += cell_value
    
    Hy_negative_sum = 0
    for row_index, col_index in indices_Hy_negative:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Hy_negative_sum += cell_value
    
    Hy_value = 20 + Hy_positive_sum - Hy_negative_sum
    variables['Hy'] = Hy_value


    # Variable Pd
    Pd_positive_sum = 0
    for row_index, col_index in indices_Pd_positive:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Pd_positive_sum += cell_value
    
    Pd_negative_sum = 0
    for row_index, col_index in indices_Pd_negative:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Pd_negative_sum += cell_value
    
    Pd_value = 8 + Pd_positive_sum - Pd_negative_sum
    variables['Pd'] = Pd_value

    # Variable Mf
    Mf_positive_sum = 0
    for row_index, col_index in indices_Mf_positive:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Mf_positive_sum += cell_value
    
    Mf_negative_sum = 0
    for row_index, col_index in indices_Mf_negative:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Mf_negative_sum += cell_value
    
    Mf_value = 17 + Mf_positive_sum - Mf_negative_sum
    variables['Mf'] = Mf_value

    # Variable Pa
    Pa_positive_sum = 0
    for row_index, col_index in indices_Pa_positive:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Pa_positive_sum += cell_value

    Pa_negative_sum = 0
    for row_index, col_index in indices_Pa_negative:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Pa_negative_sum += cell_value

    Pa_value = 8 + Pa_positive_sum - Pa_negative_sum
    variables['Pa'] = Pa_value

    # Variable Pt
    Pt_positive_sum = 0
    for row_index, col_index in indices_Pt_positive:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Pt_positive_sum += cell_value

    Pt_negative_sum = 0
    for row_index, col_index in indices_Pt_negative:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Pt_negative_sum += cell_value

    Pt_value = 2 + Pt_positive_sum - Pt_negative_sum
    variables['Pt'] = Pt_value

    # Variable Sc
    Sc_positive_sum = 0
    for row_index, col_index in indices_Sc_positive:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Sc_positive_sum += cell_value

    Sc_negative_sum = 0
    for row_index, col_index in indices_Sc_negative:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Sc_negative_sum += cell_value

    Sc_value = 2 + Sc_positive_sum - Sc_negative_sum
    variables['Sc'] = Sc_value

    # Variable Ma
    Ma_positive_sum = 0
    for row_index, col_index in indices_Ma_positive:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Ma_positive_sum += cell_value

    Ma_negative_sum = 0
    for row_index, col_index in indices_Ma_negative:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Ma_negative_sum += cell_value

    Ma_value = 8 + Ma_positive_sum - Ma_negative_sum
    variables['Ma'] = Ma_value

    # Variable Si
    Si_positive_sum = 0
    for row_index, col_index in indices_Si_positive:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Si_positive_sum += cell_value

    Si_negative_sum = 0
    for row_index, col_index in indices_Si_negative:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Si_negative_sum += cell_value

    Si_value = 14 + Si_positive_sum - Si_negative_sum
    variables['Si'] = Si_value


    # Variable Mf Gender
    Mf_Gender_sum = 0
    for row_index, col_index in indices_Mf_gender:
        if row_index < len(result_matrix) and col_index < len(columns):
            cell_value = result_matrix[row_index][col_index]
            if cell_value in [0, 1]:
                Mf_Gender_sum += cell_value

    def excel_round(value):
        """Mimic Excel's default arithmetic rounding."""
        return int(value + 0.5) if value > 0 else int(value - 0.5)

    # Now, compute adjustments based on K
    K_value = variables['K']
    adjustments = {var: 0 for var in variables.keys()}

    adjustments['Hs'] = excel_round(K_value / 2)
    adjustments['Pd'] = excel_round(0.4 * K_value)
    adjustments['Pt'] = K_value
    adjustments['Sc'] = K_value
    adjustments['Ma'] = excel_round(0.2 * K_value)

    # Adjust 'Mf' based on user's gender
    gender = user_info.get('gender', 'Other')
    Mf_Gender_sum = variables.get('Mf_Gender', 0)
    if gender == 'Male':
        adjustments['Mf'] = Mf_Gender_sum
    elif gender == 'Female':
        adjustments['Mf'] = 5 - Mf_Gender_sum
    else:
        adjustments['Mf'] = 0  # No adjustment for 'Other' gender or unknown

    # Prepare labels and total_values
    labels = [var for var in variables.keys() if var != 'Mf_Gender']
    total_values = [variables[var] + adjustments[var] for var in labels]

    return variables, adjustments, total_values, labels

def display_brut_values(user_data, user_info):
    result_matrix, columns = advanced_analysis(user_data)
    variables, adjustments, total_values, labels = compute_variables(result_matrix, columns, user_info)
    if variables is None:
        return  # Handle error case

    # Exclude 'Mf_Gender' from variables and adjustments for plotting
    variables_for_plotting = {k: v for k, v in variables.items() if k != 'Mf_Gender'}
    adjustments_for_plotting = {k: adjustments[k] for k in variables_for_plotting}

    labels = list(variables_for_plotting.keys())
    blue_values = [variables_for_plotting[var] for var in labels]
    yellow_values = [adjustments_for_plotting[var] for var in labels]
    total_values = [variables_for_plotting[var] + adjustments_for_plotting[var] for var in labels]

    plot_brut_values(labels, blue_values, yellow_values, total_values, user_info)

def display_final_values(user_data, user_info):
    result_matrix, columns = advanced_analysis(user_data)
    variables, adjustments, total_values, labels = compute_variables(result_matrix, columns, user_info)
    if variables is None:
        return  # Handle error case

    # Exclude 'Mf_Gender' from variables and adjustments for plotting
    variables_for_plotting = {k: v for k, v in variables.items() if k != 'Mf_Gender'}
    adjustments_for_plotting = {k: adjustments[k] for k in variables_for_plotting}

    labels = list(variables_for_plotting.keys())
    total_values = [variables_for_plotting[var] + adjustments_for_plotting[var] for var in labels]

    # Now, compute final values using lookup table
    final_values = {}
    gender = user_info.get('gender', 'Other')

    # Load the lookup table from JSON
    with open('Core\lookup_table.json', 'r', encoding='utf-8') as f:
        lookup_table = json.load(f)
    # Convert brut_value keys to floats
    lookup_table = {float(k): v for k, v in lookup_table.items()}

    for var, total_value in zip(labels, total_values):
        final_value = get_final_value(total_value, var, gender, lookup_table)
        if final_value is None:
            final_value = 0
        final_values[var] = final_value

    values = [final_values[var] for var in labels]

    plot_final_values(labels, values, user_info)

def excel_round(value):
    """Mimic Excel's default arithmetic rounding."""
    return int(value + 0.5) if value > 0 else int(value - 0.5)

def get_final_value(brut_value, variable, gender, lookup_table):
    """
    Lookup the final value for a given variable, brut value, and gender.
    """
    brut_value = float(brut_value)
    gender = gender[0].upper()
    if gender not in ['M', 'F']:
        return None  # Invalid gender

    # If brut_value is in the lookup table
    if brut_value in lookup_table:
        entry = lookup_table[brut_value]
    else:
        # Find the largest 'Brut' value less than or equal to brut_value
        available_bruts = sorted(lookup_table.keys())
        lower_bruts = [b for b in available_bruts if b <= brut_value]
        if lower_bruts:
            closest_brut = lower_bruts[-1]
            entry = lookup_table[closest_brut]
        else:
            # If brut_value is smaller than any available, use the smallest 'Brut'
            closest_brut = available_bruts[0]
            entry = lookup_table[closest_brut]

    # Build the key
    key = f"{variable}_{gender}"

    # Get the final value
    final_value = entry.get(key)
    return final_value

def plot_brut_values(labels, blue_values, yellow_values, total_values, user_info):
    # Plot the stacked bar chart (Original and Adjusted Values)
    plt.figure(figsize=(12, 6))
    bar_positions = range(len(labels))

    plt.bar(bar_positions, blue_values, color='blue', label='Original Value')
    plt.bar(bar_positions, yellow_values, bottom=blue_values, color='yellow', label='Adjustment')

    # Annotate values
    for pos, blue, yellow, total in zip(bar_positions, blue_values, yellow_values, total_values):
        # Convert values to integers for display
        blue_int = int(round(blue))
        yellow_int = int(round(yellow))
        total_int = int(round(total))

        # Annotate blue value in the middle of the blue bar
        if blue_int > 0:
            plt.text(pos, blue / 2, f'{blue_int}', ha='center', va='center', color='white', fontsize=10)
        # Annotate yellow value in the middle of the yellow bar (if it exists)
        if yellow_int > 0:
            plt.text(pos, blue + yellow / 2, f'{yellow_int}', ha='center', va='center', color='black', fontsize=10)
            # Annotate total value on top of the bar
            plt.text(pos, total + 0.5, f'{total_int}', ha='center', va='bottom', fontsize=10)
        else:
            # No yellow bar, no need to display the total since it's the same as the blue value
            plt.text(pos, total + 0.5, f'{total_int}', ha='center', va='bottom', fontsize=10)

    plt.xticks(bar_positions, labels)
    plt.title(f"MMPI Variables for {user_info.get('name', '')}")
    plt.ylabel('Total Score')
    plt.legend()
    plt.show()

def plot_final_values(labels, values, user_info):
    # Plot the final values in a separate graph
    plt.figure(figsize=(12, 6))
    bar_positions = range(len(labels))

    plt.bar(bar_positions, values, color='green', label='Final Value')

    # Annotate values
    for pos, value in zip(bar_positions, values):
        value_int = int(round(value))
        plt.text(pos, value_int + 0.5, f'{value_int}', ha='center', va='bottom', fontsize=10)

    plt.xticks(bar_positions, labels)
    plt.title(f"MMPI Final Variables for {user_info.get('name', '')}")
    plt.ylabel('Final Score')
    plt.legend()
    plt.show()


def show_graph(user_data, user_info):
    # Count Yes, No, and unanswered questions
    yes_count = sum(1 for q in user_data if q['Answer'] == 'Yes')
    no_count = sum(1 for q in user_data if q['Answer'] == 'No')
    unanswered_count = sum(1 for q in user_data if q['Answer'] is None or q['Answer'] == 'None')

    labels = ['Yes', 'No', 'Unanswered']
    values = [yes_count, no_count, unanswered_count]

    # Create a pie chart in English
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['green', 'red', 'gray'],
            labeldistance=1.1, pctdistance=0.85)  # Adjust label and percentage text positions

    plt.title(f"Answer Distribution for {user_info.get('name', '')}", fontsize=14)
    plt.show()

def perform_advanced_analysis(user_data, user_info):
    # Perform advanced analysis
    result_matrix, columns = advanced_analysis(user_data)

    # Display the result matrix
    display_analysis(result_matrix, columns, user_info)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_json_file_name = sys.argv[1]
    else:
        print("No user JSON file specified.")
        sys.exit(1)
    display_table(user_json_file_name)
