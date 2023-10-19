import sys, os
from datetime import datetime
import customtkinter as ctk
from PIL import Image, ImageTk

"""
    GLAOBALS
"""

BACKGROUND = "#181818"
FOREGROUND = "#37373D"
CONFIRM = "#72B062"
CONFIRM_HOVER = "#62B062"
NEUTRAL_BUTTON = "#1D69CC"
NEUTRAL_HOVER = "#0D5CBD"
CANCEL = "#FCE2DE"
CANCEL_HOVER = "#C24632"
ADMIN = "#FFF0F0"
UNDO = "#FFC813"
UNDO_HOVER = "#FAE134"

SAVE_LOCATION = "SavedCases\\"
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
UNDO_DICT = {}

"""
    End GLOBALS
"""

"""
    def commands
"""
def copy_to_clipboard():
    if internal_check_var.get() == "on":
        NOTES_ALL = ("============== Case Notes ==============\n" +
        "Name: " + text_name.get() +
        "\nCallback Number: " + text_callback.get() +
        "\n\n========================================\n" +
        "Problem Description:\n" + description.get("0.0", "end") +
        "\n\n========================================\n" +
        "Actions Taken:\n" + actions_taken.get("0.0", "end") +
        "\n\n========================================\n" +
        "After Call Summary:\n" + next_steps.get("0.0", "end") +
        "\n\n========================================\n" +
        "Internal Notes:\n" + internal_notes.get("0.0", "end"))
    else:
        NOTES_ALL = ("============== Case Notes ==============\n" +
        "Name: " + text_name.get() +
        "\nCallback Number: " + text_callback.get() +
        "\n\n========================================\n" +
        "Problem Description:\n" + description.get("0.0", "end") +
        "\n\n========================================\n" +
        "Actions Taken:\n" + actions_taken.get("0.0", "end") +
        "\n\n========================================\n" +
        "After Call Summary:\n" + next_steps.get("0.0", "end"))
    
    app.clipboard_clear()
    app.clipboard_append(NOTES_ALL) # add to clipboard
    app.update() # keeps if app crashes

def save_to_file():
    NOTES_SAVED = ("============== Case Notes ==============\n" +
        "Name: " + text_name.get() +
        "\nCallback Number: " + text_callback.get() +
        "\n\n========================================\n" +
        "Problem Description:\n" + description.get("0.0", "end") +
        "\n\n========================================\n" +
        "Actions Taken:\n" + actions_taken.get("0.0", "end") +
        "\n\n========================================\n" +
        "After Call Summary:\n" + next_steps.get("0.0", "end") +
        "\n\n========================================\n" +
        "Internal Notes:\n" + internal_notes.get("0.0", "end"))
    
    if save_check_var.get() == "off":
        pop_up = ctk.CTkToplevel()
        pop_up.configure(fg_color=BACKGROUND)
        pop_up.wm_title("Select Save Location")
        pop_up.attributes("-topmost", True)

        WIP_label = ctk.CTkLabel(pop_up, text="Work In Progress, Save to Default Location")
        WIP_label.grid(row=0, column=0, padx=75, pady=(25,0), sticky="ew")
        cancel_button = ctk.CTkButton(pop_up, text="Cancel", fg_color=NEUTRAL_BUTTON, hover_color=NEUTRAL_HOVER,
                                      command=pop_up.destroy)
        cancel_button.grid(row=1, column=0, padx=75, pady=50, sticky="ew")
    else:
        pop_up = ctk.CTkToplevel()
        pop_up.configure(fg_color=BACKGROUND)
        pop_up.wm_title("File Saver")
        pop_up.attributes("-topmost", True)

        saved_label = ctk.CTkLabel(pop_up, text=(CURRENT_PATH + "\\" + SAVE_LOCATION + "\nAdd Case Number"),
                                   font=app_font_tuple_bold)
        saved_label.grid(row=0, column=0, padx=75, pady=(25,10), sticky="ew", columnspan=2)

        case_number = ctk.CTkEntry(pop_up, width=150, height=35, fg_color=FOREGROUND, 
                         corner_radius=10, placeholder_text="Enter Case Number", font=app_font_tuple)
        case_number.grid(row=1, column=0, padx=(75,15), pady=(0,25), sticky="ew")

        submit_button = ctk.CTkButton(pop_up, text="Submit", fg_color=CONFIRM, hover_color=CONFIRM_HOVER,
                                      command=lambda: save_to_file_helper(pop_up, NOTES_SAVED, case_number.get()))
        submit_button.grid(row=1, column=1, padx=(15,75), pady=(0,25), sticky="ew")

def save_to_file_helper(window, notes, case_number_val):
    date_str_now = datetime.now()
    date_str = str(date_str_now.month) + "-" + str(date_str_now.day) + "-" + str(date_str_now.year) + "_" + str(date_str_now.hour) + "-" + str(date_str_now.minute) + "-" + str(date_str_now.minute)
    filename = str(case_number_val) + "_" + date_str
    print(filename)

    with open(f'.\SavedCases\{filename}.txt', "w") as f:
        f.write(notes)
        f.close()
    
    window.destroy()

def clear_all():
    pop_up = ctk.CTkToplevel()
    pop_up.configure(fg_color=BACKGROUND)
    pop_up.wm_title("Clear All")
    pop_up.attributes("-topmost", True)

    clear_label = ctk.CTkLabel(pop_up, text="Are you sure?", font=app_font_tuple_bold)
    clear_label.grid(row=0, column=0, padx=75, pady=(25,10), sticky="ew")

    clear_button = ctk.CTkButton(pop_up, text="Clear", fg_color=CANCEL, hover_color=CANCEL_HOVER,
                                      command=lambda: clear_all_helper(pop_up), text_color="#111111")
    clear_button.grid(row=1, column=0, padx=75, pady=50, sticky="ew")

def clear_all_helper(window):
    UNDO_DICT.update({"name": str(text_name.get())})
    UNDO_DICT.update({"callback": str(text_callback.get())})
    UNDO_DICT.update({"problem": description.get("0.0", "end").rstrip('\n')})
    UNDO_DICT.update({"actions": actions_taken.get("0.0", "end").rstrip('\n')})
    UNDO_DICT.update({"next steps": next_steps.get("0.0", "end").rstrip('\n')})
    UNDO_DICT.update({"internal": internal_notes.get("0.0", "end").rstrip('\n')})

    text_name.delete(0, "end")
    text_name.configure(placeholder_text="Enter Name")
    text_callback.delete(0, "end")
    text_callback.configure(placeholder_text="Enter Callback Number")
    description.delete("0.0", "end")
    actions_taken.delete("0.0", "end")
    next_steps.delete("0.0", "end")
    internal_notes.delete("0.0", "end")

    print(UNDO_DICT)
    undo_button.configure(state="normal")
    window.destroy()

def undo():
    if undo_button.cget("state") == "normal":
        text_name.insert(0, UNDO_DICT["name"])
        text_callback.insert(0, UNDO_DICT["callback"])
        description.insert("0.0", UNDO_DICT["problem"])
        actions_taken.insert("0.0", UNDO_DICT["actions"])
        next_steps.insert("0.0", UNDO_DICT["next steps"])
        internal_notes.insert("0.0", UNDO_DICT["internal"])

        undo_button.configure(state="disabled")
    else:
        print("nothing to undo")


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

"""
    Loading Fonts for App, Meraki use "Sharp Sans - Bold" "Sharp Sans - Thin"
    Currently doesnt work :(
"""
app_font_tuple = ("Calibri", 14)
app_font_tuple_bold = ("Calibri", 14, "bold")
app_font_subheader = ("Calibri", 18, "bold")

# Frame Defaults
app = ctk.CTk()
app.title("Case Editor")
app.geometry("650x1000")
app.configure(fg_color=BACKGROUND)
app.minsize(650, 1000)
app.maxsize(650, 1000)

app.wm_iconbitmap(resource_path("assets/editor.ico"))

taskbar_icon = ImageTk.PhotoImage(Image.open(resource_path("assets/editor.png")))
app.wm_iconphoto(True, taskbar_icon)

# Grid Configs
app.grid_columnconfigure((0), weight=1)

# App Background
background_image = ctk.CTkImage(dark_image=Image.open(resource_path("assets/CaseEditorBackground.png")), size=(650, 1000))

# Create Label for Background
background_label = ctk.CTkLabel(app, image=background_image, text="")
background_label.place(x=0, y=0)

label = ctk.CTkLabel(app, text="", fg_color="transparent")
label.grid(row=0, column=0, pady=25)

# Text Boxes
# text_name_value = text_name.get() -- Gets the text
# .delete("0.0", "end") -- self explanatory
"""
    Name Field
"""
text_name = ctk.CTkEntry(app, width=600, height=35, fg_color=FOREGROUND, 
                         corner_radius=10, placeholder_text="Enter Name", font=app_font_tuple)
text_name.grid(row=1, column=0, padx=35, pady=5, sticky="ew", columnspan=2)

"""
    Callback Number
"""
text_callback = ctk.CTkEntry(app, height=35, fg_color=FOREGROUND, 
                             corner_radius=10, placeholder_text="Call Back Number", font=app_font_tuple)
text_callback.grid(row=2, column=0, padx=35, pady=5, sticky="ew", columnspan=2)

"""
    Adding label for "Problem Description"
"""
problem_label = ctk.CTkLabel(app, text="Problem Description", fg_color="transparent", font=app_font_subheader,
                             justify="left", anchor="w")
problem_label.grid(row=3, column=0, padx=35, pady=0, sticky="ew", columnspan=2)

"""
    Problem Description
"""
description = ctk.CTkTextbox(app, width=600, height=70, fg_color=FOREGROUND, 
                           corner_radius=5, font=app_font_tuple, wrap='word')
description.grid(row=4, column=0, padx=35, pady=7, sticky="ew", columnspan=2)

"""
    Adding Label for "Actions Taken"
"""
action_label = ctk.CTkLabel(app, text="Actions Taken", fg_color="transparent", font=app_font_subheader,
                             justify="left", anchor="w")
action_label.grid(row=5, column=0, padx=35, pady=0, sticky="ew", columnspan=2)

"""
    Actions Taken
"""
actions_taken = ctk.CTkTextbox(app, width=600, height=250, fg_color=FOREGROUND, 
                           corner_radius=5, font=app_font_tuple, wrap='word')
actions_taken.grid(row=6, column=0, padx=35, pady=7, sticky="ew", columnspan=2)

"""
    Label for "Next Steps"
"""
next_label = ctk.CTkLabel(app, text="Next Steps", fg_color="transparent", font=app_font_subheader,
                             justify="left", anchor="w")
next_label.grid(row=7, column=0, padx=35, pady=0, sticky="ew", columnspan=2)

"""
    Next Steps
"""
next_steps = ctk.CTkTextbox(app, width=600, height=70, fg_color=FOREGROUND, 
                           corner_radius=5, font=app_font_tuple, wrap='word')
next_steps.grid(row=8, column=0, padx=35, pady=7, sticky="ew", columnspan=2)

"""
    Internal Notes
"""
internal_label = ctk.CTkLabel(app, text="Internal Notes", fg_color="transparent", font=app_font_subheader,
                             justify="left", anchor="w")
internal_label.grid(row=9, column=0, padx=35, pady=0, sticky="ew")

internal_notes = ctk.CTkTextbox(app, width=280, height=220, fg_color=ADMIN, border_width=2, border_color=CANCEL_HOVER,
                                corner_radius=2, font=app_font_tuple_bold, wrap="word", text_color=BACKGROUND)
internal_notes.grid(row=10, column=0, padx=(35,0), pady=7, sticky="ew")

"""
    Tabbed view for buttons and additional info
"""
button_tabs = ctk.CTkTabview(app, segmented_button_selected_color=NEUTRAL_BUTTON,
                             segmented_button_selected_hover_color=NEUTRAL_HOVER,
                             segmented_button_unselected_color=FOREGROUND,
                             segmented_button_unselected_hover_color=NEUTRAL_HOVER)
button_tabs.grid(row=9, column=1, padx=(10,35), pady=7, sticky="ew", rowspan=2)

"""
    Tabs with their buttons
"""
tab_1 = button_tabs.add("Options")
tab_2 = button_tabs.add("Utilities")

"""
    Tab 1 Buttons
"""
clipboard_button = ctk.CTkButton(tab_1, anchor="center", 
                                 fg_color=NEUTRAL_BUTTON, 
                                 hover_color=NEUTRAL_HOVER, 
                                 text="Copy To Clipboard", font=app_font_tuple_bold,
                                 command=copy_to_clipboard)
clipboard_button.grid(row=0, column=0, padx=(3,0), pady=5)


internal_check_var = ctk.StringVar(value="off")
internal_checkbox = ctk.CTkCheckBox(tab_1, text="Copy Internal", variable=internal_check_var,
                                    onvalue="on", offvalue="off", fg_color=NEUTRAL_BUTTON,
                                    hover_color=NEUTRAL_HOVER, font=app_font_tuple_bold,
                                    checkbox_width=20, checkbox_height=20)
internal_checkbox.grid(row=0, column=1, padx=(10,10), pady=5)


save_button = ctk.CTkButton(tab_1, width=clipboard_button.cget("width"), anchor="center",
                            fg_color=CONFIRM, hover_color=CONFIRM_HOVER,
                            text="Save To File", font=app_font_tuple_bold,
                            command=save_to_file)
save_button.grid(row=1, column=0, padx=(3,0), pady=5)

save_check_var = ctk.StringVar(value="on")
save_checkbox = ctk.CTkCheckBox(tab_1, text="Default Location", variable=save_check_var,
                                    onvalue="on", offvalue="off", fg_color=NEUTRAL_BUTTON,
                                    hover_color=NEUTRAL_HOVER, font=app_font_tuple_bold,
                                    checkbox_width=20, checkbox_height=20)
save_checkbox.grid(row=1, column=1,padx=(15,0), pady=5)


clear_button = ctk.CTkButton(tab_1, width=clipboard_button.cget("width"), anchor="center",
                            fg_color=CANCEL_HOVER, hover_color=CANCEL,
                            text="Clear", font=app_font_tuple_bold,
                            command=clear_all, text_color=BACKGROUND)
clear_button.grid(row=2, column=0, padx=(3,0), pady=5)

undo_button = ctk.CTkButton(tab_1, width=clipboard_button.cget("width"), anchor="center",
                            fg_color=UNDO, hover_color=UNDO_HOVER,
                            text="Undo", font=app_font_tuple_bold,
                            command=undo, text_color=BACKGROUND)
undo_button.configure(state="disabled")
undo_button.grid(row=3, column=0, padx=(3,0), pady=5)


# App runtime loop
app.mainloop()


"""
    pyinstaller --noconfirm --onedir --windowed --add-data "c:/users/mark/appdata/roaming/python/python310/site-packages/customtkinter;customtkinter/;assets/"  "editor_v2.py"
    run auto-py-to-exe in terminal
"""