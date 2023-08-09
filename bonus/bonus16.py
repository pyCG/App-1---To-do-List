import PySimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", 
                   layout = [[label1, input1, choose_button1],
                             [label2, input2, choose_button2],
                             [compress_button]])

window.read()
window.close()

#%%
import PySimpleGUI as sg 

label1 = sg.Text("Enter feet")
input1 = sg.Input()

label2 = sg.Text("Enter inches")
input2 = sg.Input()

convert_button = sg.Button("Convert")
s
window = sg.Window("Convertor",
                   layout = [[label1, input1],
                             [label2, input2],
                             [convert_button]])

window.read()
window.close()