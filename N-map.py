import PySimpleGUI as sg
import subprocess

def run_nmap(target):
    try:
        # Use subprocess to run Nmap command and capture the output
        result_bytes = subprocess.check_output([r'C:\Program Files (x86)\Nmap\nmap.exe', '-sV', target])
        result_str = result_bytes.decode('utf-8')
        return result_str
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Set the dark theme with SkyBlue4 color for the GUI
sg.theme('DarkBlue4')

# Define the layout of the GUI with square buttons
layout = [
    [sg.Text('Target IP:'), sg.InputText(key='target_ip')],
    [sg.Button('Scan', size=(10, 1))],
    [sg.Multiline('', key='output', size=(80, 20), autoscroll=True)],
]

# Create the GUI window
window = sg.Window('Vulnerability Scanner with Visual Reporting', layout)

# Event loop to handle user interactions
while True:
    event, values = window.read()

    # Close the window if the user clicks the close button
    if event == sg.WIN_CLOSED:
        break

    # Perform a scan when the user clicks the "Scan" button
    if event == 'Scan':
        target_ip = values['target_ip']
        scan_result = run_nmap(target_ip)
        
        # Update the output field with the scan result
        window['output'].update(scan_result)

# Close the GUI window when the loop exits
window.close()
