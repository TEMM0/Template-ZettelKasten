import PySimpleGUI as sg
from file_creator import Note
import time
import os


metafile = open("metadata", "r")
saved_vault = metafile.readline()
metafile.close()
vault_path = sg.popup_get_folder('Choose location of vault', default_path=saved_vault)

if not vault_path:
    sys.exit(0)

metafile = open("metadata", "w")
print(vault_path)
metafile.write(vault_path)
metafile.close()

os.chdir(vault_path)

# Define the window's contents
layout = [[sg.Text("Please, enter name of the zettel-note")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(100,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    if event == 'Ok':
      Zettel=Note()
      Zettel.write_to_file(str(values['-INPUT-']))
      del Zettel
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Success, ' + values['-INPUT-'] + " was created")

# Finish up by removing from the screen
window.close()