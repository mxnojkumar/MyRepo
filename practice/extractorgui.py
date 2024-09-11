import FreeSimpleGUI as sg
from extractorfunc import extract_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.InputText(key="files_input")
button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Choose the destination:  ")
input2 = sg.InputText(key="folder_input")
button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Extract")
output_label = sg.Text(key="output")

window = sg.Window("Zip Extractor", 
                   layout=[[label1, input1, button1], 
                           [label2, input2, button2], 
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == "Extract":
        archivepath = values["archive"]
        folder = values["folder"]
    
    if archivepath and folder:
            extract_archive(archivepath, folder)
            window["output"].update(value="Extraction completed!")
               
    else:
        window["output"].update(value="Please select file and destination folder.")
    
window.close()