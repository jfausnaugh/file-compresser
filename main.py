import PySimpleGUI as sg
from zip_creator import make_zip
from zip_extractor import extract_zip

# Create widgets

label1 = sg.Text("Select files to compress: ",
                 background_color="light gray", text_color="black")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select the destination folder:",
                 background_color="light gray", text_color="black")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green",
                       background_color="light gray")

extract_button = sg.Button("Extract")

# create window

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, extract_button, output_label]],
                   background_color="light gray", button_color="royal blue")

while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    if event == "Compress":
        make_zip(filepaths, folder)
        window["output"].update(value="Compression completed!")
    elif event == "Extract":
        zip_path = values["files"]
        extract_zip(zip_path, folder)
        window["output"].update(value="Extraction completed!")
    match event:
        case sg.WIN_CLOSED:
            break

window.close()

