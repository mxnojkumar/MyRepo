import FreeSimpleGUI as sg
from compressfunc import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.InputText(key="files_input")
button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Choose the destination:  ")
input2 = sg.InputText(key="folder_input")
button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output")

window = sg.Window("File Compressor", 
                   layout=[[label1, input1, button1], 
                           [label2, input2, button2], 
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == "Compress":
        filepaths = values["files"].split(';')
        folder = values["folder"]
    
    if filepaths and folder:
            make_archive(filepaths, folder)
            window["output"].update(value="Compression Successful.")
               
    else:
        window["output"].update(value="Please select files and destination folder.")
    
window.close()