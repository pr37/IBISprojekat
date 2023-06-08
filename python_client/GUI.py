import tkinter as tk
from tkinter import ttk,Text
import socket
from PIL import Image, ImageTk #pip install pillow


def flowsensorBTN():
    result = client_call("GET FLOW_SENSOR ALL")  # Call the function
    result_label.config(text=result)  # Update the label with the returned string

def temperatureBTN():
    result = client_call("GET TEMPERATURE ALL")
    result_label.config(text=result)  # Update the label with the returned string

def levelsensorBTN():
    result = client_call("GET LEVEL_SENSOR ALL")  # Call the function
    result_label.config(text=result)  # Update the label with the returned string

def pressuresensorBTN():
    result = client_call("GET PRESSURE_SENSOR ALL")  # Call the function
    result_label.config(text=result)  # Update the label with the returned string
def Send_id_for_water_level():
    text = T.get(1.0, "end-1c")
    result = client_call("SEND DAM ID FOR WATER LEVEL,"+text)  # Call the function
    result_label.config(text=result)

def Send_id_for_pressure():
    text = T1.get(1.0, "end-1c")
    result = client_call("SEND DAM ID FOR PRESSURE,"+text)  # Call the function
    result_label.config(text=result)

def Send_id_for_valve_state():
    text = T2.get(1.0, "end-1c")
    result = client_call("SEND DAM ID VALVE STATE,"+text)  # Call the function
    result_label.config(text=result)

def Change_valve_state_by_id():
    id_Dam = T3.get(1.0, "end-1c")
    valve_state = option_var_valve.get()
    result = client_call("CHANGE VALVE STATE BY ID," + id_Dam + "," + valve_state)  # Call the function
    result_label.config(text=result)

def stressBTN():
    result = client_call("GET STRESS ALL")
    result_label.config(text=result)

def emergencyShutDownBTN():
    selected_option = option_var.get()
    result = client_call("SHUTDOWN "+selected_option)

def client_call(api_string):
    HOST, PORT = "localhost", 9999
    #HOST, PORT = "192.168.10.10", 9999

    #LIST OF API CALLS
    get_flow = bytes(api_string.encode())
    get_temp = bytes(api_string.encode())
    get_stress = bytes(api_string.encode())

    get_level = bytes(api_string.encode())
    get_pressure = bytes(api_string.encode())
    get_water_level_specific_dam = bytes(api_string.encode())
    get_water_presssure_specific_dam = bytes(api_string.encode())
    get_valve_specific_dam = bytes(api_string.encode())

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))

        #sock.sendall(get_flow)
        #sock.sendall(get_temp)
       # sock.sendall(get_stress)
        #sock.sendall(get_water_level_specific_dam)
        sock.sendall(get_valve_specific_dam)

        # Receive data from the server and shut down
        received = sock.recv(1024)
        return received

# Create the main window
window = tk.Tk()
window.geometry("600x300")
window.configure(bg="#ECECEC")
# Create a button
style = ttk.Style()
style.configure("TButton", background="#3498db", foreground="white", font=("Helvetica", 12))

options = ["Dam 1", "Dam 2", "Dam 3", "Dam 4"]

# Create a variable to store the selected option
option_var = tk.StringVar(window)

# Create a menu list of string options
option_menu = ttk.OptionMenu(window, option_var, options[1], *options)
option_menu.grid(row=0, column=3, padx=10, pady=10)
button2 = ttk.Button(window, text="Shut Down", command=emergencyShutDownBTN)
button2.grid(row=0, column=5, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=1, column=0, padx=10, pady=10)
button = tk.Button(window, text="Get All Flow Sensor Readings", command=flowsensorBTN)
button.grid(row=0, column=0, padx=10, pady=10)

tempButton = tk.Button(window, text="Get All Water Temperatures", command=temperatureBTN)
tempButton.grid(row=0, column=3, padx=10, pady=10)

stressButton = tk.Button(window, text="Get All Stresses", command=stressBTN)
stressButton.grid(row=0, column=4, padx=10, pady=10)

tempButton.grid(row=0, column=7, padx=10, pady=10)


result_label = tk.Label(window, text="")
result_label.grid(row=1, column=0, padx=10, pady=10)
button = tk.Button(window, text="Get All Level Sensor Readings", command=levelsensorBTN)
button.grid(row=0, column=1, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=1, column=0, padx=10, pady=10)
button = tk.Button(window, text="Get All Pressure Sensor Readings", command=pressuresensorBTN)
button.grid(row=0, column=2, padx=10, pady=10)

label1 = ttk.Label(window, text="Dam 1")
label1.grid(row=2, column=0)
label2 = ttk.Label(window, text="Dam 2")
label2.grid(row=2, column=1)
label3 = ttk.Label(window, text="Dam 3")
label3.grid(row=2, column=2)
label4 = ttk.Label(window, text="Dam 4")
label4.grid(row=2, column=3)
#TODO menjati ove slike prema statusu brane
image1 = Image.open("damOK.png")
image1 = image1.resize((50, 50))  # Resize the image to 100x100 pixels
image1 = ImageTk.PhotoImage(image1)
image_label1 = ttk.Label(window, image=image1)
image_label1.grid(row=3, column=0, padx=10, pady=10)  # Position the first image label

image2 = Image.open("damOK.png")
image2 = image2.resize((50, 50))  # Resize the image to 100x100 pixels
image2 = ImageTk.PhotoImage(image2)
image_label2 = ttk.Label(window, image=image2)
image_label2.grid(row=3, column=1, padx=10, pady=10)  # Position the second image label

image3 = Image.open("damOK.png")
image3 = image3.resize((50, 50))  # Resize the image to 100x100 pixels
image3 = ImageTk.PhotoImage(image3)
image_label3 = ttk.Label(window, image=image3)
image_label3.grid(row=3, column=2, padx=10, pady=10)  # Position the third image label

image4 = Image.open("damOK.png")
image4 = image4.resize((50, 50))  # Resize the image to 100x100 pixels
image4 = ImageTk.PhotoImage(image4)
image_label4 = ttk.Label(window, image=image4)
image_label4.grid(row=3, column=3, padx=10, pady=10)

T = Text(window,width=5,height=1)
T.grid(row=5,column=0)
label5 = ttk.Label(window, text="Unesite id brane za nivo vode")
label5.grid(row=4, column=0)
button = tk.Button(window, text="Posalji", command=Send_id_for_water_level)
button.grid(row=6, column=0)

T1 = Text(window,width=5,height=1)
T1.grid(row=5,column=1)
label6 = ttk.Label(window, text="Unesite id brane za pritisak vode")
label6.grid(row=4, column=1)
button = tk.Button(window, text="Posalji", command=Send_id_for_pressure)
button.grid(row=6, column=1)

T2 = Text(window,width=5,height=1)
T2.grid(row=5,column=2)
label7 = ttk.Label(window, text="Unesite id brane za ocitavanje stanja ventila")
label7.grid(row=4, column=2)
button = tk.Button(window, text="Posalji", command=Send_id_for_valve_state)
button.grid(row=6, column=2)

options_valve = ["open", "close"]

# Create a variable to store the selected option
option_var_valve = tk.StringVar(window)

# Create a menu list of string options
label8 = ttk.Label(window, text="Unesite Id brane za promenu stanja ventila")
label8.grid(row=4, column=3)
T3 = Text(window,width=5,height=1)
T3.grid(row=5,column=3)
option_menu = ttk.OptionMenu(window, option_var_valve, options_valve[1], *options_valve)
option_menu.grid(row=6, column=3)
button = tk.Button(window, text="Posalji", command=Change_valve_state_by_id)
button.grid(row=7, column=3)

# Start the main event loop
window.mainloop()
