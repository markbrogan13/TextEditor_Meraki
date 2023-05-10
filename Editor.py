from datetime import datetime
import PySimpleGUI as sg
from sqlalchemy import null
import os

theme_change = null

def main(theme):
    theme_list = [
        'Black', ['Black', 'DarkBlack', 'DarkBlack1'],
        'Grey', ['DarkGrey1', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkGrey10'],
        'Blue', ['BlueMono', 'BluePurple', 'DarkBlue1', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4'],
        'Extras', ['BrightColors', 'DefaultNoMoreNagging', 'Purple', 'Python', 'PythonPlus', 'TealMono', 'Topanga']
    ]

    theme_event = theme_list[1] + theme_list[3] + theme_list[5]

    menu_layout = [
        ['File', ['Open', 'Save', '---', 'Exit']],
        ['Tools', ['Character Count']],
        ['Themes', theme_list]
    ]

    sg.theme(theme)
    layout = [
        [sg.Menu(menu_layout)],
        [sg.Text('Case Template', key = '-DOCNAME-')],
        [sg.Text('Name:'), sg.InputText(key='-NAME-')],
        [sg.Text('Call Back #:'), sg.InputText(key='-NUMBER-')],
        [sg.Text('Problem Description:')],
        [sg.Multiline(no_scrollbar=True, size=(80,2), key='-PROB-', expand_x=True)],
        [sg.Text('Actions Taken:')],
        [sg.Multiline(no_scrollbar=False, size=(80,5), key='-ACTIONS-', expand_x=True, expand_y=True)],
        [sg.Text('Next Steps:')],
        [sg.Multiline(no_scrollbar=False, size=(80,1), key='-NEXT-', expand_x=True, expand_y=True)],
        [sg.Text('INTERNAL COMMENTS:')],
        [sg.Multiline(no_scrollbar=False, size=(80,3), key='-INTERNAL-', expand_x=True, expand_y=True)],
        [sg.Button(button_text='Save to Clipboard'), sg.Button(button_text='Copy Internal Comments'), sg.Button(button_text='Clear', button_color='red'), sg.Button(button_text='Undo'), sg.Button(button_text='Save to File', button_color='green')],
    ]

    default_font = ("Arial", 14)
    window = sg.Window('Case Editor', layout, resizable=True, size=(675, 800), font=default_font)
    m1 = window['-NAME-']
    undo_event = null

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        # Unimplemented dunno how to update it :c
        if event in theme_event:
            theme_change = values # TODO: Implement the re-fill of someone had theme changed and had items written
            window.close()
            main(event)
            print(event)
        
        if event == 'Character Count':
            full_text = values['-NAME-'] + values['-NUMBER-'] + values['-PROB-'] + values['-ACTIONS-'] + values['-NEXT-']
            x, y = sg.Window.current_location(window)
            popup_x = x + 150
            popup_y = y + 375
            sg.popup('Total Characters: ' + str(len(full_text) + 61), location=(popup_x, popup_y))

        if event == 'Save to Clipboard':
            # full_text = values['-NAME-'] + values['-NUMBER-'] + values['-PROB-'] + values['-ACTIONS-'] + values['-NEXT-']
            full_text = "========================================\n"
            full_text += f"Name: {values['-NAME-']}\nCall Back #: {values['-NUMBER-']}\n"
            full_text += "\n========================================\n"
            full_text += f"Problem Description:\n{values['-PROB-']}\n"
            full_text += "\n========================================\n"
            full_text += f"Actions Taken:\n{values['-ACTIONS-']}\n"
            full_text += "\n========================================\n"
            full_text += f"Next Steps:\n{values['-NEXT-']}"
            full_text += "\n========================================"

            sg.clipboard_set(full_text)
        
        if event == 'Copy Internal Comments':
            internal_text = values['-INTERNAL-']

            sg.clipboard_set(internal_text)
        
        if event == 'Clear':
            undo_event = values
            x, y = sg.Window.current_location(window)
            popup_x = x + 150
            popup_y = y + 375
            check = sg.popup_yes_no("Are you sure?", title='Clear Confirm', font=default_font, location=(popup_x + 50, popup_y))
            
            if str(check) == "Yes":
                window['-NAME-'].update('')
                window['-NUMBER-'].update('')
                window['-PROB-'].update('')
                window['-ACTIONS-'].update('')
                window['-NEXT-'].update('')
                window['-INTERNAL-'].update('')
                m1.set_focus()

        if event == 'Undo':
            if undo_event == null:
                undo_event = values
            window['-NAME-'].update(undo_event['-NAME-'])
            window['-NUMBER-'].update(undo_event['-NUMBER-'])
            window['-PROB-'].update(undo_event['-PROB-'])
            window['-ACTIONS-'].update(undo_event['-ACTIONS-'])
            window['-NEXT-'].update(undo_event['-NEXT-'])
            window['-INTERNAL-'].update(undo_event['-INTERNAL-'])
        
        if event == 'Save to File':
            full_text = "========================================\n"
            full_text += f"Name: {values['-NAME-']}\nCall Back #: {values['-NUMBER-']}\n"
            full_text += "\n========================================\n"
            full_text += f"Problem Description:\n{values['-PROB-']}\n"
            full_text += "\n========================================\n"
            full_text += f"Actions Taken:\n{values['-ACTIONS-']}\n"
            full_text += "\n========================================\n"
            full_text += f"Next Steps:\n{values['-NEXT-']}"
            full_text += "\n========================================\n"
            full_text += f"INTERNAL COMMENTS:\n{values['-INTERNAL-']}"

            x,y = sg.Window.current_location(window)
            popup_x = x + 150
            popup_y = y + 375
            print(x,y) # x += 150, y += 375
            case_number = sg.popup_get_text('Enter a Case Number:', title="Save to File", font=default_font, location=(popup_x, popup_y))

            if case_number == None or case_number == '':
                sg.popup_auto_close('No case number input -- File Not Saved', title='You\'ve Hit my Trap Card', font=default_font, location=(popup_x + 50, popup_y))    
            else:
                date_str_now = datetime.now()
                date_str = str(date_str_now.month) + "-" + str(date_str_now.day) + "-" + str(date_str_now.year) + "_" + str(date_str_now.hour) + ":" + str(date_str_now.minute) + ":" + str(date_str_now.minute)
                filename = str(case_number) + "_" + date_str
                print(filename)

                with open(f'./SavedCases/{filename}.txt', "w") as f:
                    f.write(full_text)
                    f.close()

            
    window.close()

if __name__ == "__main__":
    theme_default = 'DarkGrey10'
    main(theme_default)

"""
Notes and features:
- Would like to add spell check [N/A completion]
- Adding pictures to the fields [Unknown if possible]
- adding an icon for the app [OS Icon Completed 07/24/2022, TODO: App side application]
- reset cursor if possible [Completed 07/24/2022]

APP NAME: TBD
EXE instructions: pyinstaller -i "assets/editor.ico" Editor.py --onefile -w 
DMG instructions: python3 /Users/mbrogan/Library/Python/3.9/bin/py2applet --make-setup Editor.py --iconfile assets/editor.icns && python3 setup.py py2app -A

NOTE: Install all requirements for this App to work, crazy thought LMAO
"""