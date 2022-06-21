import PySimpleGUI as sg
from sqlalchemy import null

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
        [sg.Multiline(no_scrollbar=False, size=(80,5), key='-NEXT-', expand_x=True, expand_y=True)],
        [sg.Button(button_text='Save to Clipboard'), sg.Button(button_text='Clear'), sg.Button(button_text='Undo')]
    ]

    window = sg.Window('Case Editor', layout, resizable=True, size=(675, 800))
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
            sg.popup('Total Characters: ' + str(len(full_text) + 61))

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
        
        if event == 'Clear':
            undo_event = values
            window['-NAME-'].update('')
            window['-NUMBER-'].update('')
            window['-PROB-'].update('')
            window['-ACTIONS-'].update('')
            window['-NEXT-'].update('')

        if event == 'Undo':
            window['-NAME-'].update(undo_event['-NAME-'])
            window['-NUMBER-'].update(undo_event['-NUMBER-'])
            window['-PROB-'].update(undo_event['-PROB-'])
            window['-ACTIONS-'].update(undo_event['-ACTIONS-'])
            window['-NEXT-'].update(undo_event['-NEXT-'])

    window.close()

if __name__ == "__main__":
    theme_default = 'DarkGrey10'
    main(theme_default)

"""
Notes and features:
- Would like to add spell check
- Undo Button [DONE 6/20/2022]
- smoother experience and fully app wrapped [EXE DONE 6/20/2022]
- Change Theme feature [DONE 6/20/2022]


EXE instructions: pyinstaller Editor.py --onefile -w 
DMG instructions:
"""