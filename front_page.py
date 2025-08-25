import os
import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
import json
from tkinter import simpledialog
from tkcalendar import DateEntry


# Styling variables
font_style = ('Helvetica', 14)
button_color = '#0078D7'
text_color = 'white'
frame_bg_color = 'white'
button_padx = 20
button_pady = 10
button_width = 10
button_height = 3

root = tk.Tk()
root.title('Front Page')
root.geometry('1400x800')

# Set up base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_DIR = os.path.join(BASE_DIR, 'Users')
CORE_DIR = os.path.join(BASE_DIR, 'Core')
DATA_FILE = os.path.join(BASE_DIR, 'user_data.json')

# Ensure Users directory exists
if not os.path.exists(USERS_DIR):
    os.makedirs(USERS_DIR)

# Load user data
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)

def load_user_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_user_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def create_new_user_file(username, age, folder_number, date, gender):
    # Map Arabic gender to English
    gender_map = {'ذكر': 'Male', 'أنثى': 'Female'}
    gender_english = gender_map.get(gender, 'Other')
    
    user_data = load_user_data()
    new_user = {
        "name": username,
        "age": age,
        "folder_number": folder_number,
        "date": date,
        "gender": gender_english
    }
    user_data.append(new_user)
    save_user_data(user_data)

    # Load the core questions data
    core_json_path = os.path.join(CORE_DIR, 'core_data.json')
    with open(core_json_path, 'r', encoding='utf-8') as f:
        core_data = json.load(f)

    # Initialize user data
    user_questions = [{'English Question Number': item['English Question Number'],
                       
                       'Arabic Question Number': item['Arabic Question Number'],
                       'Y': item['Y'],
                       'Question Text': item['Question Text'],
                       'Answer': None} for item in core_data]

    # Prepare user file data
    user_file_data = {
        "user_info": new_user,
        "questions": user_questions
    }

    # Save user data to new JSON file
    new_json_filename = f"{username}.json"
    new_json_filepath = os.path.join(BASE_DIR, 'MMPI_JSON', new_json_filename)
    with open(new_json_filepath, 'w', encoding='utf-8') as f:
        json.dump(user_file_data, f, ensure_ascii=False, indent=4)

    message_label.config(text=f"Created new JSON file for {username}", fg='green')
    open_main_ui(new_json_filename)


def open_main_ui(user_json_filename):
    root.destroy()
    import MainUI
    MainUI.run_main_ui(user_json_filename)

def setup_new_user_frame():
    # Clear any existing content in the frame
    for widget in new_user_frame.winfo_children():
        widget.destroy()

    # Colors and styles
    label_bg_color = '#ffffff'  # Light grey background for labels
    entry_bg_color = '#ffffff'  # White background for entry
    button_bg_color = '#0078D7'  # Blue background for buttons
    button_fg_color = '#ffffff'  # White text for buttons
    frame_padding = 20

    # Configuring the frame
    new_user_frame.config(bg=label_bg_color, padx=frame_padding, pady=frame_padding)

    # Update and repack the global message label
    message_label.config(bg=label_bg_color)
    message_label.pack(in_=new_user_frame, pady=(5, 10))

    # Label and entry for the username
    entry_label = tk.Label(new_user_frame, text="أدخل اسمك", font=('Helvetica', 14), bg=label_bg_color)
    entry_label.pack(pady=(0, 10))  # Add padding below the label
    username_entry = tk.Entry(new_user_frame, font=('Helvetica', 14), bg=entry_bg_color, borderwidth=2, relief="groove")
    username_entry.pack(pady=(0, 20))
    username_entry.focus_set()

    # Label and entry for the age
    age_label = tk.Label(new_user_frame, text="أدخل العمر", font=('Helvetica', 14), bg=label_bg_color)
    age_label.pack(pady=(0, 10))
    age_entry = tk.Entry(new_user_frame, font=('Helvetica', 14), bg=entry_bg_color, borderwidth=2, relief="groove")
    age_entry.pack(pady=(0, 20))

    # Label and entry for the folder number
    folder_label = tk.Label(new_user_frame, text="أدخل رقم المجلد", font=('Helvetica', 14), bg=label_bg_color)
    folder_label.pack(pady=(0, 10))
    folder_entry = tk.Entry(new_user_frame, font=('Helvetica', 14), bg=entry_bg_color, borderwidth=2, relief="groove")
    folder_entry.pack(pady=(0, 20))

    # Label for the date
    date_label = tk.Label(new_user_frame, text="أدخل التاريخ", font=('Helvetica', 14), bg=label_bg_color)
    date_label.pack(pady=(0, 10))
    # DateEntry widget for the date
    date_entry = DateEntry(new_user_frame, font=('Helvetica', 14), width=16, background='darkblue',
                           foreground='white', borderwidth=2, relief="groove", date_pattern='dd/MM/yyyy')
    date_entry.pack(pady=(0, 20))

    # Label and option menu for gender
    gender_label = tk.Label(new_user_frame, text="أدخل الجنس", font=('Helvetica', 14), bg=label_bg_color)
    gender_label.pack(pady=(0, 10))

    gender_var = tk.StringVar()
    gender_var.set('اختر الجنس')  # Default value

    gender_options = ['ذكر', 'أنثى']
    gender_menu = tk.OptionMenu(new_user_frame, gender_var, *gender_options)
    gender_menu.config(font=('Helvetica', 14), bg=entry_bg_color, borderwidth=2, relief="groove")
    gender_menu.pack(pady=(0, 20))

    # Function to call when the create user button is clicked
    def on_create_clicked():
        username = username_entry.get().strip()
        age = age_entry.get().strip()
        folder_number = folder_entry.get().strip()
        date = date_entry.get_date().strftime('%d/%m/%Y')  # Get date from DateEntry
        gender = gender_var.get().strip()

        # Validate age input
        if not age.isdigit() or not (0 <= int(age) <= 200):
            message_label.config(text="الرجاء إدخال عمر صالح", fg='red')
            return  # Stop execution if the age is invalid

        # Check if any other field is missing
        missing_fields = []
        if not username:
            missing_fields.append("الاسم")
        if not folder_number:
            missing_fields.append("رقم المجلد")
        if not date:
            missing_fields.append("التاريخ")
        if not gender or gender == 'اختر الجنس':
            missing_fields.append("الجنس")

        if missing_fields:
            missing_fields_str = ', '.join(missing_fields)
            message_label.config(text=f"الرجاء إدخال {missing_fields_str}", fg='red')
        else:
            # All fields are filled, proceed to create user
            message_label.config(text=".تم إنشاء مستخدم جديد بنجاح!", fg='green')  # Display success message
            create_new_user_file(username, int(age), folder_number, date, gender)


    # Button to confirm the creation of a new user
    create_button = tk.Button(new_user_frame, text="إنشاء مستخدم", command=on_create_clicked, font=('Helvetica', 14),
                              bg=button_bg_color, fg=button_fg_color, borderwidth=2, relief="raised")
    create_button.pack(pady=(0, 10), ipadx=10, ipady=5)  # Add internal padding to make the button more prominent

def show_new_user_frame():
    welcome_label.pack_forget() 
    prev_user_frame.pack_forget()
    new_user_frame.pack(fill=tk.BOTH, expand=True)

def show_prev_user_frame():
    welcome_label.pack_forget() 
    new_user_frame.pack_forget()
    listbox.delete(0, tk.END)
    user_data = load_user_data()
    for user in user_data:
        user_filename = f"{user['name']}.json"
        user_filepath = os.path.join(BASE_DIR, 'MMPI_JSON', user_filename)
        if os.path.exists(user_filepath):
            with open(user_filepath, 'r', encoding='utf-8') as f:
                user_file_data = json.load(f)
            # Handle both old and new formats
            if isinstance(user_file_data, list):
                # Old format: user_file_data is a list of questions
                questions = user_file_data
                user_info = user  # Use info from user_data.json
                # Update user_file_data to new format
                user_file_data = {
                    "user_info": user_info,
                    "questions": questions
                }
                # Save the updated user_file_data back to the file
                with open(user_filepath, 'w', encoding='utf-8') as f_out:
                    json.dump(user_file_data, f_out, ensure_ascii=False, indent=4)
            else:
                # New format: user_file_data is a dictionary
                questions = user_file_data.get('questions', [])
            # Check if all questions have been answered
            if all(q.get('Answer') in ['Yes', 'No'] for q in questions):
                status = "Completed"
            else:
                status = "In Progress"
        else:
            status = "No Data"
        listbox.insert(tk.END, f"Name: {user['name']}, Age: {user['age']}, Folder: {user['folder_number']}, Date: {user.get('date', '')}, Gender: {user.get('gender', '')}, Status: {status}")
    prev_user_frame.pack(fill=tk.BOTH, expand=True)



def on_prev_user_selected(event=None):
    try:
        selected_indices = listbox.curselection()
        if len(selected_indices) != 1:
            messagebox.showerror("Selection Error", "Please select a single user to open.")
            return
        selected_index = selected_indices[0]
        user_data = load_user_data()
        selected_user = user_data[selected_index]
        selected_file = f"{selected_user['name']}.json"
        open_main_ui(selected_file)
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a user from the list.")


def export_selected_users():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showerror("Selection Error", "Please select at least one user to export.")
        return

    # Ask the user to choose a directory to save the exported files
    from tkinter import filedialog
    export_dir = filedialog.askdirectory(title="Select Export Directory")
    if not export_dir:
        # User cancelled the dialog
        return

    user_data = load_user_data()
    success_count = 0
    failed_users = []

    for index in selected_indices:
        selected_user = user_data[index]
        user_filename = f"{selected_user['name']}.json"
        user_filepath = os.path.join(BASE_DIR, 'MMPI_JSON', user_filename)
        if os.path.exists(user_filepath):
            try:
                # Copy the file to the selected directory
                import shutil
                destination = os.path.join(export_dir, user_filename)
                shutil.copy(user_filepath, destination)
                success_count += 1
            except Exception as e:
                failed_users.append(selected_user['name'])
        else:
            failed_users.append(selected_user['name'])

    if success_count > 0:
        messagebox.showinfo("Export Successful", f"Successfully exported {success_count} user(s).")
    if failed_users:
        failed_users_str = ", ".join(failed_users)
        messagebox.showerror("Export Failed", f"Failed to export the following users: {failed_users_str}")


def import_users():
    from tkinter import filedialog
    file_paths = filedialog.askopenfilenames(title="Select User Files", filetypes=(("JSON Files", "*.json"),))
    if not file_paths:
        # User cancelled the dialog
        return

    user_data = load_user_data()
    existing_user_names = [user['name'] for user in user_data]
    imported_users = []
    skipped_users = []

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                user_file_data = json.load(f)
            user_info = user_file_data.get('user_info', {})
            user_name = user_info.get('name')
            if not user_name:
                messagebox.showerror("Import Error", f"File {os.path.basename(file_path)} does not contain user information.")
                continue
            if user_name in existing_user_names:
                # User already exists, skip
                skipped_users.append(user_name)
                continue
            # Copy the file to MMPI_JSON directory
            import shutil
            destination = os.path.join(BASE_DIR, 'MMPI_JSON', f"{user_name}.json")
            shutil.copy(file_path, destination)
            # Add user info to user_data.json
            user_data.append(user_info)
            existing_user_names.append(user_name)
            imported_users.append(user_name)
        except Exception as e:
            messagebox.showerror("Import Error", f"Failed to import {os.path.basename(file_path)}: {e}")
    # Save the updated user data
    save_user_data(user_data)
    # Display import summary
    messages = []
    if imported_users:
        messages.append(f"Successfully imported: {', '.join(imported_users)}")
    if skipped_users:
        messages.append(f"Skipped existing users: {', '.join(skipped_users)}")
    if messages:
        messagebox.showinfo("Import Summary", "\n".join(messages))
    else:
        messagebox.showinfo("Import", "No users were imported.")
    # Refresh the user list
    show_prev_user_frame()


def delete_selected_users():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showerror("Selection Error", "Please select at least one user to delete.")
        return

    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected user(s)? This action cannot be undone.")
    if not confirm:
        return

    user_data = load_user_data()
    users_to_delete = [user_data[index] for index in selected_indices]

    for user in users_to_delete:
        user_name = user['name']
        user_filename = f"{user_name}.json"
        user_filepath = os.path.join(BASE_DIR, 'MMPI_JSON', user_filename)
        # Remove user file
        if os.path.exists(user_filepath):
            os.remove(user_filepath)
        # Remove user from user_data
        user_data.remove(user)

    # Save updated user data
    save_user_data(user_data)
    messagebox.showinfo("Delete Successful", "Selected users have been deleted.")
    # Refresh the user list
    show_prev_user_frame()

def clear_selection():
    listbox.selection_clear(0, tk.END)

def copy_selected_user():
    selected_indices = listbox.curselection()
    if len(selected_indices) != 1:
        messagebox.showerror("Selection Error", "Please select a single user to copy.")
        return

    index = selected_indices[0]
    user_data = load_user_data()
    selected_user = user_data[index]
    original_name = selected_user['name']

    # Prompt for a new name
    new_name = simpledialog.askstring("Copy User", "Enter a new name for the copied user:")
    if not new_name:
        return  # User cancelled or didn't enter a name

    # Check if the new name already exists
    existing_user_names = [user['name'] for user in user_data]
    if new_name in existing_user_names:
        messagebox.showerror("Name Conflict", "A user with that name already exists.")
        return

    # Copy user data
    new_user = selected_user.copy()
    new_user['name'] = new_name

    # Save the new user to user_data.json
    user_data.append(new_user)
    save_user_data(user_data)

    # Copy the user's JSON file
    import shutil
    original_filename = f"{original_name}.json"
    new_filename = f"{new_name}.json"
    original_filepath = os.path.join(BASE_DIR, 'MMPI_JSON', original_filename)
    new_filepath = os.path.join(BASE_DIR, 'MMPI_JSON', new_filename)
    if os.path.exists(original_filepath):
        shutil.copy(original_filepath, new_filepath)
        # Update the 'name' in the copied JSON file
        with open(new_filepath, 'r', encoding='utf-8') as f:
            user_file_data = json.load(f)
        user_file_data['user_info']['name'] = new_name
        with open(new_filepath, 'w', encoding='utf-8') as f:
            json.dump(user_file_data, f, ensure_ascii=False, indent=4)
        messagebox.showinfo("Copy Successful", f"User '{original_name}' has been copied to '{new_name}'.")
        # Refresh the user list
        show_prev_user_frame()
    else:
        messagebox.showerror("File Error", f"Original user file '{original_filename}' not found.")

bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Create a welcome message label with Arabic text
welcome_text = "MMPI مرحبًا بكم في اختبار\n\n\n\nالرجاء النقر على 'مستخدم جديد' لإنشاء ملف شخصي جديد\n\nأو النقر على 'مستخدم سابق' لاختيار ملف موجود"
welcome_label = tk.Label(root, text=welcome_text, font=('Helvetica', 16), bg='white', justify=tk.CENTER)
welcome_label.pack(fill=tk.BOTH, expand=True, pady=100)

new_user_button = tk.Button(bottom_frame, text="مستخدم جديد", bg=button_color, fg=text_color,
                            font=font_style, command=show_new_user_frame,
                            width=button_width, height=button_height)
new_user_button.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

prev_user_button = tk.Button(bottom_frame, text="مستخدم سابق", bg=button_color, fg=text_color,
                             font=font_style, command=show_prev_user_frame,
                             width=button_width, height=button_height)
prev_user_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

new_user_frame = tk.Frame(root)
# Create a global message_label so it can be accessed anywhere
message_label = tk.Label(root, text="", font=('Helvetica', 12), fg='red')

setup_new_user_frame()

prev_user_frame = tk.Frame(root)
listbox = Listbox(prev_user_frame, bg=frame_bg_color, font=font_style, selectmode=tk.EXTENDED)
listbox.bind('<Double-1>', on_prev_user_selected)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = Scrollbar(prev_user_frame, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(prev_user_frame)
button_frame.pack(side=tk.BOTTOM, fill=tk.X)

# OK button at the top of prev_user_frame
prev_user_ok_button = tk.Button(prev_user_frame, text="Open", bg=button_color, fg=text_color, font=font_style, command=on_prev_user_selected)
prev_user_ok_button.pack(side=tk.TOP, fill=tk.X, padx=button_padx, pady=button_pady)

# Other buttons in button_frame at the bottom
prev_user_clear_button = tk.Button(button_frame, text="Clear Selection", bg=button_color, fg=text_color, font=font_style, command=clear_selection)
prev_user_clear_button.pack(side=tk.TOP, fill=tk.X, padx=button_padx, pady=button_pady)

prev_user_export_button = tk.Button(button_frame, text="Export", bg=button_color, fg=text_color, font=font_style, command=export_selected_users)
prev_user_export_button.pack(side=tk.TOP, fill=tk.X, padx=button_padx, pady=button_pady)

prev_user_import_button = tk.Button(button_frame, text="Import", bg=button_color, fg=text_color, font=font_style, command=import_users)
prev_user_import_button.pack(side=tk.TOP, fill=tk.X, padx=button_padx, pady=button_pady)

prev_user_copy_button = tk.Button(button_frame, text="Copy User", bg=button_color, fg=text_color, font=font_style, command=copy_selected_user)
prev_user_copy_button.pack(side=tk.TOP, fill=tk.X, padx=button_padx, pady=button_pady)

prev_user_delete_button = tk.Button(button_frame, text="Delete", bg='red', fg=text_color, font=font_style, command=delete_selected_users)
prev_user_delete_button.pack(side=tk.TOP, fill=tk.X, padx=button_padx, pady=button_pady)

root.mainloop()
