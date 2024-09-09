import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.InputText()
button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Choose the destination:  ")
input2 = sg.InputText()
button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[label1, input1, button1], 
                                              [label2, input2, button2], 
                                              [compress_button]])

window.read()
window.close()