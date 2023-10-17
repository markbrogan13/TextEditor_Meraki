import customtkinter as ctk
from PIL import Image, ImageFont

"""
    Custom Color HEX values that will be uesd across the app
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

"""
    End Color Globals
"""

"""
    Loading Fonts for App, Meraki use "Sharp Sans - Bold" "Sharp Sans - Thin"
    Currently doesnt work :(
"""
meraki_font = ImageFont.truetype(font="fonts/SharpSans-Thin.ttf", size=24)
meraki_font_bold = ImageFont.truetype(font="fonts/SharpSans-Book.ttf", size=24)
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

# Grid Configs
app.grid_columnconfigure((0), weight=1)

# App Background
background_image = ctk.CTkImage(dark_image=Image.open("assets/CaseEditorBackground.png"), size=(650, 1000))

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
button_tabs.grid(row=9, column=1, padx=35, pady=7, sticky="ew", rowspan=2)

"""
    Tabs with their buttons
"""
tab_1 = button_tabs.add("Options")
tab_2 = button_tabs.add("Utilities")

# App runtime loop
app.mainloop()
