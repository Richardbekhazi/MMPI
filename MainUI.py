import os
import json
import tkinter as tk
import subprocess
from tkinter import font
from PIL import Image, ImageOps, ImageTk
from tkinter import ttk
from tkinter import messagebox


def run_main_ui(user_json_file_name):
    # Initialize variables
    current_question_index = None
    test_completed = False
    firework_label = None  # Define firework_label in the enclosing scope
    close_button = None    # Define close_button in the enclosing scope
    finish_modifying_button = None  # For Finish Modifying button
    options_frame = None  # For options after test completion
    modifying_answers = False  # Flag to indicate if we are modifying answers

    # Load core questions data from JSON
    script_dir = os.path.dirname(os.path.abspath(__file__))
    core_json_path = os.path.join(script_dir, 'Core', 'core_data.json')
    with open(core_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Load or create user data JSON
    user_json_path = os.path.join(script_dir, 'MMPI_JSON', user_json_file_name)
    if os.path.exists(user_json_path):
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
                # Save the updated user_file_data back to the file
                with open(user_json_path, 'w', encoding='utf-8') as f_out:
                    json.dump(user_file_data, f_out, ensure_ascii=False, indent=4)
            else:
                # New format: user_file_data is a dictionary
                user_info = user_file_data.get('user_info', {})
                user_data = user_file_data.get('questions', [])
    else:
        # Initialize user data with answers set to None
        user_data = [{'English Question Number': item['English Question Number'],
                      'Arabic Question Number': item['Arabic Question Number'],
                      'Y': item['Y'],
                      'Question Text': item['Question Text'],
                      'Answer': None} for item in data]
        user_info = {}  # Empty dict if no user info

        # Save the new user data to a JSON file
        user_file_data = {
            "user_info": user_info,
            "questions": user_data
        }
        with open(user_json_path, 'w', encoding='utf-8') as f:
            json.dump(user_file_data, f, ensure_ascii=False, indent=4)

    # Initialize the UI
    root = tk.Tk()
    root.title(f"MMPI Questions - {user_info.get('name', '')}")
    root.geometry('1000x800')  # Increased width to accommodate the navigation pane

    # Create a frame to hold user info at the top
    user_info_frame = tk.Frame(root)
    user_info_frame.pack(pady=10)

    # Display user info labels
    name_label = tk.Label(user_info_frame, text=f"{user_info.get('name', 'Guest')}", font=('Helvetica', 16))
    name_label.pack(side=tk.LEFT, padx=10)

    # Initialize progress bar variables
    total_questions = len(user_data)
    answered_questions = sum(1 for q in user_data if q['Answer'] in ['Yes', 'No'])

    # Function to check if the test is completed					
    def is_test_completed():
        return all(q['Answer'] in ['Yes', 'No'] for q in user_data)
    
    # Function to save the user's answer to the JSON file
    def save_answer():
        # Update the user_file_data with the latest questions and user info
        user_file_data['questions'] = user_data
        user_file_data['user_info'] = user_info
        with open(user_json_path, 'w', encoding='utf-8') as f:
            json.dump(user_file_data, f, ensure_ascii=False, indent=4)

																										 

    # Function to convert numbers to Arabic numerals
    def convert_to_arabic_numerals(input_number):
        arabic_numerals = {
            '0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤',
            '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'
        }
        return ''.join(arabic_numerals.get(x, x) for x in str(input_number))

    # Function to update the question number label
    def update_question_number():
        if current_question_index is not None:
            question_number_text = "السؤال رقم {}{}".format(
                convert_to_arabic_numerals(user_data[current_question_index]['Y']),
                user_data[current_question_index]['Arabic Question Number']
            )
            question_number_label.config(text=question_number_text)
        else:
            question_number_label.config(text="All questions answered")

    # Function to finalize the test
    def finalize_test():
        nonlocal test_completed, current_question_index, options_frame
        if any(q['Answer'] is None for q in user_data):
            # There are still unanswered questions
            current_question_index = find_next_unanswered(0)
            update_question_label()
            highlight_answer()
        else:
            if not test_completed:
                question_number_label.config(text='شكراً للمشاركة')
                question_label.config(text='تم الإجابة على جميع الأسئلة')
                show_fireworks()
                test_completed = True
                # Remove any existing widgets from control_frame
                for widget in control_frame.winfo_children():
                    widget.destroy()
                # Display options in control_frame
                options_frame = tk.Frame(control_frame)
                options_frame.pack(fill=tk.X, pady=10)
                show_graph_button = tk.Button(options_frame, text='عرض النتائج', command=show_graph, font=button_font, bg='blue', fg='white')
                show_graph_button.pack(pady=5, fill=tk.X)
                modify_answers_button = tk.Button(options_frame, text='تعديل الإجابات', command=modify_answers, font=button_font, bg='green', fg='white')
                modify_answers_button.pack(pady=5, fill=tk.X)
                return_main_menu_button = tk.Button(options_frame, text='العودة إلى القائمة الرئيسية', command=close_application, font=button_font, bg='red', fg='white')
                return_main_menu_button.pack(pady=5, fill=tk.X)

		

    # Function to show the graph
    def show_graph():
                # Call the back_end.py script after finalizing the test
                script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
                back_end_path = os.path.join(script_dir, 'back_end.py')  # Construct the full path to back_end.py
                subprocess.Popen(["python", back_end_path, user_json_file_name])  # Pass the user JSON file name

    def modify_answers():
        nonlocal test_completed, options_frame, finish_modifying_button, current_question_index, firework_label, close_button, modifying_answers
        # Destroy the options frame
        options_frame.destroy()
        # Destroy the fireworks image if it exists
        if firework_label is not None:
            firework_label.destroy()
            firework_label = None
        # Destroy the close button if it exists
        if close_button is not None:
            close_button.destroy()
            close_button = None
        # Show frames and question label again
        button_frame.pack(fill=tk.X, side=tk.TOP, pady=10)
        question_label.pack(fill="both", expand=True, padx=20, pady=10)
        bottom_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=(5, 20))
        # Set flags
        test_completed = False
        modifying_answers = True
        # Add 'Finish Modifying' button
        finish_modifying_button = tk.Button(control_frame, text='إنهاء التعديل',
                                            command=finish_modifying, font=button_font, bg='blue', fg='white')
        finish_modifying_button.pack(pady=10)
        # Update question label and highlight answer
        current_question_index = 0  # Start from the first question
        update_question_label()
        highlight_answer()

    def finish_modifying():
        nonlocal finish_modifying_button, modifying_answers
        finish_modifying_button.destroy()
        modifying_answers = False  # Exiting modifying answers mode
        finalize_test()

    # Function to close the application
    def close_application():
        root.destroy()
        # Run front_page.py
        script_dir = os.path.dirname(os.path.abspath(__file__))
        front_page_path = os.path.join(script_dir, 'front_page.py')
        subprocess.Popen(["python", front_page_path])				   

    # Function to update the question label
    def update_question_label():
        if current_question_index is not None and current_question_index < len(user_data):
            question_label.config(text=user_data[current_question_index]['Question Text'])
            update_question_number()
            # Update the listbox selection
            question_listbox.selection_clear(0, tk.END)
            question_listbox.selection_set(current_question_index)
            question_listbox.activate(current_question_index)
            question_listbox.see(current_question_index)  # Ensure the selection is visible
        else:
            finalize_test()

    # Function to highlight the selected answer
    def highlight_answer():
        # Reset buttons to default colors
        yes_button.config(bg='green', fg='white')
        no_button.config(bg='red', fg='white')
        skip_button.config(bg='orange', fg='white')

        # Retrieve the stored answer
        answer = user_data[current_question_index]['Answer']

        # Highlight the button corresponding to the stored answer and gray out the others
        if answer == 'Yes':
            yes_button.config(bg='green', fg='white')
            skip_button.config(bg='gray', fg='light gray')
            no_button.config(bg='gray', fg='light gray')
        elif answer == 'No':
            no_button.config(bg='red', fg='white')
            skip_button.config(bg='gray', fg='light gray')
            yes_button.config(bg='gray', fg='light gray')
        elif answer is None:
            # If no answer, keep all buttons in default colors
            pass
        else:
            skip_button.config(bg='orange', fg='white')
            yes_button.config(bg='gray', fg='light gray')
            no_button.config(bg='gray', fg='light gray')

    # Function to update the progress bar
    def update_progress_bar():
        # Count the number of answered questions (excluding skipped questions)
        answered = sum(1 for q in user_data if q['Answer'] in ['Yes', 'No'])
        # Calculate the percentage
        if total_questions > 0:
            progress_percentage = (answered / total_questions) * 100
        else:
            progress_percentage = 0
        # Update the progress variable
        progress_var.set(progress_percentage)

    # Function to handle the selection of a question from the listbox
    def on_question_select(event):
        nonlocal current_question_index
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            current_question_index = index
            update_question_label()
            highlight_answer()

    # Function to update the listbox entry
    def update_listbox_entry(index):
        answer = user_data[index]['Answer']
        if answer == 'Yes':
            answer_status = "✔"
        elif answer == 'No':
            answer_status = "❌"
        else:
            answer_status = "➖"  # Symbol for unanswered or skipped

        # Construct the Arabic question number
        question_number = "{}{}".format(
            convert_to_arabic_numerals(user_data[index]['Y']),
            user_data[index]['Arabic Question Number']
        )
        question_text = f"{answer_status} :السؤال رقم {question_number}"

        question_listbox.delete(index)
        question_listbox.insert(index, question_text)

    # Function to handle the Back button
    def handle_back():
        nonlocal current_question_index
        if current_question_index > 0:
            current_question_index -= 1
            update_question_label()
            highlight_answer()
        else:
            messagebox.showinfo("Info", "This is the first question.")

    # Function to handle the Forward button
    def handle_forward():
        nonlocal current_question_index
        if current_question_index < len(user_data) - 1:
            current_question_index += 1
            update_question_label()
            highlight_answer()
        else:
            messagebox.showinfo("Info", "This is the last question.")

    # Function to find the next unanswered question
    def find_next_unanswered(start_index):
        for i in range(start_index, len(user_data)):
            if user_data[i]['Answer'] is None:
                return i
        return None

    # Function to handle the answer
    def handle_answer(answer):
        nonlocal current_question_index, test_completed
        if test_completed and not modifying_answers:
            return

        user_data[current_question_index]['Answer'] = answer
        save_answer()
        update_progress_bar()
        update_listbox_entry(current_question_index)  # Update the listbox entry

        if modifying_answers:
            # Stay on the current question or navigate as per user input
            update_question_label()
            highlight_answer()
        else:
            # Move to the next unanswered question
            current_question_index = find_next_unanswered(current_question_index + 1)
            if current_question_index is not None:
                update_question_label()
                highlight_answer()
            else:
                finalize_test()


    # Function to handle skipping a question
    def handle_skip():
        nonlocal current_question_index, test_completed
        if test_completed:
            return

        # Ensure that 'Answer' remains None for skipped questions
        user_data[current_question_index]['Answer'] = None
        update_listbox_entry(current_question_index)

        # Move to the next question
        current_question_index = find_next_unanswered(current_question_index + 1)
        if current_question_index is not None:
            update_question_label()
            highlight_answer()
        else:
            finalize_test()

    # Function to display fireworks image upon completion
    def show_fireworks():
        nonlocal firework_label, close_button
        # Hide frames and question label
        bottom_frame.pack_forget()
        button_frame.pack_forget()
        question_label.pack_forget()
        # Remove any existing widgets from control_frame
        for widget in control_frame.winfo_children():
            widget.destroy()
        # Display fireworks
        image = Image.open(firework_path)
        firework_img = ImageTk.PhotoImage(image)
        firework_label = tk.Label(question_frame, image=firework_img)
        firework_label.image = firework_img  # Keep a reference
        firework_label.pack(expand=True)
        # Create a Close button in control_frame
        close_button = tk.Button(control_frame, text='إغلاق', command=close_application,
                                font=button_font, bg='blue', fg='white')
        close_button.pack(pady=10)

    # Paths to images
    firework_path = os.path.join(script_dir, 'Images', 'firework.jpg')
    loading_path = os.path.join(script_dir, 'Images', 'loading.png')
    back_image_path = os.path.join(script_dir, 'Images', 'Back.png')

    # Load and configure the back and forward button images
    forward_img = Image.open(back_image_path)
    back_img = ImageOps.mirror(forward_img)  # Flip the image for forward button

    # Resize the images before creating PhotoImage objects
    button_image_size = (100, 100)
    try:
        resample_method = Image.Resampling.LANCZOS
    except AttributeError:
        resample_method = Image.LANCZOS  # For older Pillow versions

    back_img_resized = back_img.resize(button_image_size, resample_method)
    forward_img_resized = forward_img.resize(button_image_size, resample_method)

    back_photo = ImageTk.PhotoImage(back_img_resized)
    forward_photo = ImageTk.PhotoImage(forward_img_resized)

    # Styling for the question text
    question_font = font.Font(family='Helvetica', size=20, weight='bold')

    # Styling for the buttons
    button_font = font.Font(family='Helvetica', size=16, weight='bold')
    button_width = 15
    button_height = 3
    button_padx = 10
    button_pady = 10

    root.protocol("WM_DELETE_WINDOW", lambda: close_application())

    # Create a progress bar
    progress_var = tk.DoubleVar()
    style = ttk.Style()
    style.theme_use('default')
    style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')

    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, style="green.Horizontal.TProgressbar")
    progress_bar.pack(fill=tk.X, padx=20, pady=10)

    update_progress_bar()

    # Create a main frame to hold both the navigation pane and the question area
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    # Create the navigation pane (Listbox) on the right
    nav_frame = tk.Frame(main_frame, width=200)
    nav_frame.pack(side=tk.RIGHT, fill=tk.Y)

    # Create the listbox and scrollbar
    question_listbox = tk.Listbox(nav_frame, width=30)
    question_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(nav_frame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    question_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=question_listbox.yview)

    # Populate the listbox with Arabic question numbers
    for idx, item in enumerate(user_data):
        answer = item['Answer']
        if answer == 'Yes':
            answer_status = "✔"
        elif answer == 'No':
            answer_status = "❌"
        else:
            answer_status = "➖"  # Symbol for unanswered or skipped

        # Construct the Arabic question number
        question_number = "{}{}".format(
            convert_to_arabic_numerals(item['Y']),
            item['Arabic Question Number']
        )
        question_text = f"{answer_status} :السؤال رقم {question_number}"
        question_listbox.insert(tk.END, question_text)

    question_listbox.bind('<<ListboxSelect>>', on_question_select)

    # Initialize current question index
    current_question_index = find_next_unanswered(0)

    # Create a new frame inside question_frame at the top for the navigation buttons
    question_frame = tk.Frame(main_frame, bg="white", borderwidth=0)
    question_frame.pack(side=tk.LEFT, fill="both", expand=True)



    button_frame = tk.Frame(question_frame, bg="white", borderwidth=0)
    button_frame.pack(fill=tk.X, side=tk.TOP, pady=10)
    button_frame.grid_columnconfigure(0, weight=1)  # Configure for equal distribution
    button_frame.grid_columnconfigure(1, weight=1)  # Configure for equal distribution
    button_frame.grid_columnconfigure(2, weight=1)  # Configure for equal distribution

    root.back_photo = back_photo
    root.forward_photo = forward_photo

    # Place the "Back" button on the left side of the button frame using grid
    back_button = tk.Button(button_frame, image=back_photo, command=handle_back, bg="white", borderwidth=0, highlightthickness=0)
    back_button.image = back_photo  # keep a reference
    back_button.grid(row=0, column=0, sticky='w')  # Use grid to place it

    # Place the question number label in the middle of the button frame using grid
    question_number_label = tk.Label(button_frame, text='', bg='white', font=question_font)
    question_number_label.grid(row=0, column=1, sticky='ew')  # Use grid to place it

    # Place the "Forward" button on the right side of the button frame using grid
    forward_button = tk.Button(button_frame, image=forward_photo, command=handle_forward, bg="white", borderwidth=0, highlightthickness=0)
    forward_button.image = forward_photo  # keep a reference
    forward_button.grid(row=0, column=2, sticky='e')  # Use grid to place it

    # The question label is packed below the button_frame within the question_frame
    question_label = tk.Label(question_frame, text='', wraplength=700, font=question_font, bg='white', anchor='center', justify='center')
    question_label.pack(fill="both", expand=True, padx=20, pady=10)

    # Create a frame within question_frame to hold controls like Finish Modifying button
    control_frame = tk.Frame(question_frame)
    control_frame.pack(side=tk.BOTTOM, fill=tk.X)

    # Buttons for Yes (نعم), Skip (تخطي السؤال), or No (كلا)
    bottom_frame = tk.Frame(question_frame)
    bottom_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=(5, 20))
    bottom_frame.columnconfigure(0, weight=1)
    bottom_frame.columnconfigure(1, weight=1)
    bottom_frame.columnconfigure(2, weight=1)

    yes_button = tk.Button(bottom_frame, text='نعم', bg='green', fg='white',
                        width=button_width, height=button_height,
                        font=button_font, command=lambda: handle_answer('Yes'))
    yes_button.grid(row=0, column=2, padx=button_padx, pady=button_pady, sticky='ew')

    skip_button = tk.Button(bottom_frame, text='تخطي السؤال', bg='orange', fg='white',
                            width=button_width, height=button_height,
                            font=button_font, command=handle_skip)
    skip_button.grid(row=0, column=1, padx=button_padx, pady=button_pady, sticky='ew')

    no_button = tk.Button(bottom_frame, text='كلا', bg='red', fg='white',
                        width=button_width, height=button_height,
                        font=button_font, command=lambda: handle_answer('No'))
    no_button.grid(row=0, column=0, padx=button_padx, pady=button_pady, sticky='ew')

    # Start the test by updating the question label
    if current_question_index is not None:
        update_question_label()
        highlight_answer()
    else:
        finalize_test()

    root.mainloop()

if __name__ == "__main__":
    run_main_ui("Test.json")
