import FreeSimpleGUI as sg
from convertorfunc import convert

sg.theme("Black")

label1 = sg.Text("Enter feet:")
input1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_label = sg.Text(key="output", text_color='green')

window = sg.Window("Convertor", 
                   layout=[[label1, input1], 
                           [label2, input2], 
                           [convert_button, exit_button, output_label]])
# window["output"].update(value=)

while True:
    event, values = window.read()
    print(event)
    print(values)
    
    try:
        feet = float(values["feet"])
        inches = float(values["inches"])
        op = convert(feet, inches)
        window["output"].update(value=op)
        
    except ValueError:
        sg.popup("Please provide two numbers.", font=("Helvetica", 10))
        
    match event:
        case "Exit":
            break

window.close()