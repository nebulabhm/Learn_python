import PySimpleGUI as sg

layout = [
    [sg.Output(size=(50, 1), key='number', pad=(5,5))],
    [sg.Button('7'), sg.Button('8'), sg.Button('9')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3')]
]

window = sg.Window('计算器', layout)

t = ''

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:
        t = t + event
        window['number'].update(t)