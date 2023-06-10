import tkinter as tk
from tkinter import ttk
import socket
from PIL import Image, ImageTk

dam_states = ["inactive", "inactive", "inactive", "inactive"]

# Function to make API call to the server
def client_call(api_string):
    HOST, PORT = "localhost", 9999

    # List of API calls
    api_calls = {
        "GET FLOW_SENSOR ALL": bytes(api_string.encode()),
        "GET TEMPERATURE ALL": bytes(api_string.encode()),
        "GET LEVEL_SENSOR ALL": bytes(api_string.encode()),
        "GET PRESSURE_SENSOR ALL": bytes(api_string.encode()),
        "GET STRESS ALL": bytes(api_string.encode()),
        "GET VALVE_STATE ALL": bytes(api_string.encode()),
        "GET PUMP_STATE ALL": bytes(api_string.encode()),
        "SEND DAM ID FOR WATER LEVEL": bytes(api_string.encode()),
        "SEND DAM ID FOR PRESSURE": bytes(api_string.encode()),
        "SEND DAM ID VALVE STATE": bytes(api_string.encode()),
        "CHANGE VALVE STATE BY ID": bytes(api_string.encode()),
        "CHANGE PUMP STATE BY ID": bytes(api_string.encode()),
        "GET DAM STATE": bytes(api_string.encode())
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(api_calls[api_string])

        received = sock.recv(1024)
        return received

def client_call2(api_string):
    HOST, PORT = "localhost", 9999
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(api_string.encode()))
        received = sock.recv(1024)
        return received


def update_images():
    for i, val in enumerate(dam_states):
        if val == "inactive":
            image = Image.open(image_files[2])
            image = image.resize((50, 50))
            IMAGES[i] = ImageTk.PhotoImage(image)
        elif val == "active":
            image = Image.open(image_files[0])
            image = image.resize((50, 50))
            IMAGES[i] = ImageTk.PhotoImage(image)
        elif val == "damaged":
            image = Image.open(image_files[1])
            image = image.resize((50, 50))
            IMAGES[i] = ImageTk.PhotoImage(image)


# Function to update the GUI with real-time data
def update_data():
    # Make API calls to update the data
    result_flowsensor = client_call("GET FLOW_SENSOR ALL")
    result_temperature = client_call("GET TEMPERATURE ALL")
    result_levelsensor = client_call("GET LEVEL_SENSOR ALL")
    result_pressuresensor = client_call("GET PRESSURE_SENSOR ALL")
    result_stress = client_call("GET STRESS ALL")
    result_valves = client_call("GET VALVE_STATE ALL")
    result_pumps = client_call("GET PUMP_STATE ALL")

    # Update the result label with the new data
    result_label_flowsensor.config(text=result_flowsensor)
    result_label_temperature.config(text=result_temperature)
    result_label_levelsensor.config(text=result_levelsensor)
    result_label_pressuresensor.config(text=result_pressuresensor)
    result_label_stress.config(text=result_stress)
    result_label_valves.config(text=result_valves)
    result_label_pumps.config(text=result_pumps)

    byte_states = client_call("GET DAM STATE")
    str_states = byte_states.decode("utf-8")
    for i in range(4):
        indx = i + 1
        dam_states[i] = str_states.split(' ')

    if (str_states.split(' ')[0] == "emergency"):
        result_label_dam_state.config(text="Dam 1: " + "emergency shut down" + "\n" + "Dam 2: " + "emergency shut down" + "\n" + "Dam 3: " + "emergency shut down" + "\n" + "Dam 4: " + "emergency shut down")
    else:
        result_label_dam_state.config(text="Dam 1: " + str(str_states.split(' ')[0])+ "\n" + "Dam 2: " + str(str_states.split(' ')[1]) + "\n" + "Dam 3: " + str(str_states.split(' ')[2]) + "\n"+ "Dam 4: " + str(str_states.split(' ')[3]))

    update_images()

    # Schedule the next update after 2 seconds
    window.after(3000, update_data)


def shutdown_system():
    api_string = "SHUTDOWN"
    result = client_call2(api_string)
    print(result)


def change_valve_state():
    selected_valve_state1 = selected_valve_state.get()
    selected_dam_id1 = selected_dam_id.get()
    api_string = f"CHANGE VALVE STATE BY ID {selected_dam_id1} {selected_valve_state1}"
    result = client_call2(api_string)
    print(result)

def change_pump_state():
    selected_pump_state1 = selected_pump_state.get()
    selected_dam_id1 = selected_dam_id2.get()
    api_string = f"CHANGE PUMP STATE BY ID {selected_dam_id1} {selected_pump_state1}"
    result = client_call2(api_string)
    print(result)


# Create the main window
window = tk.Tk()
window.geometry("900x600")
window.configure(bg="#ECECEC")

# Create a frame for the header
header_frame = tk.Frame(window, bg="#ECECEC")
header_frame.pack(pady=20)

# Header label
header_label = ttk.Label(header_frame, text="Dam Monitoring System", font=("Helvetica", 20))
header_label.pack()

# Create a frame for the content
content_frame = tk.Frame(window, bg="#ECECEC")
content_frame.pack(pady=20)

# Create a frame for the data
data_frame = tk.Frame(content_frame, bg="#ECECEC")
data_frame.grid(row=0, column=0, padx=10, pady=10)

# Create a frame for the dam status images
dam_frame = tk.Frame(content_frame, bg="#ECECEC")
dam_frame.grid(row=0, column=2, padx=10, pady=10)

# Create sections for different API calls
section_frame_flowsensor = tk.Frame(data_frame, bg="#ECECEC")
section_frame_flowsensor.grid(row=0, column=0, pady=10, padx=10)

section_frame_temperature = tk.Frame(data_frame, bg="#ECECEC")
section_frame_temperature.grid(row=0, column=1, pady=10, padx=10)

section_frame_levelsensor = tk.Frame(data_frame, bg="#ECECEC")
section_frame_levelsensor.grid(row=1, column=0, pady=10, padx=10)

section_frame_pressuresensor = tk.Frame(data_frame, bg="#ECECEC")
section_frame_pressuresensor.grid(row=1, column=1, pady=10, padx=10)

section_frame_stress = tk.Frame(data_frame, bg="#ECECEC")
section_frame_stress.grid(row=2, column=0, pady=10, padx=10)

section_frame_valves = tk.Frame(data_frame, bg="#ECECEC")
section_frame_valves.grid(row=2, column=1, pady=10, padx=10)

section_frame_pumps = tk.Frame(data_frame, bg="#ECECEC")
section_frame_pumps.grid(row=3, column=1, pady=10, padx=10)

section_frame_dam_state = tk.Frame(data_frame, bg="#ECECEC")
section_frame_dam_state.grid(row=3, column=0, pady=10, padx=10)

style = ttk.Style()
style.configure("Red.TButton", foreground="red")
button_shutdown = ttk.Button(dam_frame, text="Shutdown", command=shutdown_system)
button_shutdown.config(style="Red.TButton")
button_shutdown.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

# Result labels for each API call
result_label_flowsensor = tk.Label(section_frame_flowsensor, text="", bg="#ECECEC")
result_label_flowsensor.pack()

result_label_temperature = tk.Label(section_frame_temperature, text="", bg="#ECECEC")
result_label_temperature.pack()

result_label_levelsensor = tk.Label(section_frame_levelsensor, text="", bg="#ECECEC")
result_label_levelsensor.pack()

result_label_pressuresensor = tk.Label(section_frame_pressuresensor, text="", bg="#ECECEC")
result_label_pressuresensor.pack()

result_label_stress = tk.Label(section_frame_stress, text="", bg="#ECECEC")
result_label_stress.pack()

result_label_valves = tk.Label(section_frame_valves, text="", bg="#ECECEC")
result_label_valves.pack()

result_label_pumps = tk.Label(section_frame_pumps, text="", bg="#ECECEC")
result_label_pumps.pack()

result_label_dam_state = tk.Label(section_frame_dam_state, text="", bg="#ECECEC")
result_label_dam_state.pack()

# Dam status images
image_files = ["damOK.png", "danger.png", "damClosed.png"]  # Replace with actual image filenames

image_labels = []
image_files = ["damOK.png", "danger.png", "damClosed.png"]  # Replace with actual image filenames


#for i, filename in enumerate(image_files):
image1 = Image.open(image_files[0])
image1 = image1.resize((50, 50))
image1 = ImageTk.PhotoImage(image1)
image_label1 = ttk.Label(dam_frame, image=image1)
image_label1.image = image1  # Store a reference to the image to prevent garbage collection
image_label1.grid(row=5, column=0, padx=10, pady=10)
image_labels.append(image_label1)
label1 = ttk.Label(dam_frame, text="Dam 1")  # Add the label text here
label1.grid(row=6, column=0)

image2 = Image.open(image_files[0])
image2 = image2.resize((50, 50))
image2 = ImageTk.PhotoImage(image2)
image_label2 = ttk.Label(dam_frame, image=image2)
image_label2.image = image1  # Store a reference to the image to prevent garbage collection
image_label2.grid(row=5, column=1, padx=10, pady=10)
image_labels.append(image_label2)
label2 = ttk.Label(dam_frame, text="Dam 2")  # Add the label text here
label2.grid(row=6, column=1)

image3 = Image.open(image_files[0])
image3 = image3.resize((50, 50))
image3 = ImageTk.PhotoImage(image3)
image_label3 = ttk.Label(dam_frame, image=image3)
image_label3.image = image3  # Store a reference to the image to prevent garbage collection
image_label3.grid(row=5, column=2, padx=10, pady=10)
image_labels.append(image_label3)
label3 = ttk.Label(dam_frame, text="Dam 3")  # Add the label text here
label3.grid(row=6, column=2)

image4 = Image.open(image_files[0])
image4 = image4.resize((50, 50))
image4 = ImageTk.PhotoImage(image4)
image_label4 = ttk.Label(dam_frame, image=image4)
image_label4.image = image4  # Store a reference to the image to prevent garbage collection
image_label4.grid(row=5, column=3, padx=10, pady=10)
image_labels.append(image_label4)
label4 = ttk.Label(dam_frame, text="Dam 4")  # Add the label text here
label4.grid(row=6, column=3)

IMAGES = [image1,image2,image3,image4]

# Drop-down menu for valve states
valve_states = ["open", "close"]
selected_valve_state = tk.StringVar()
selected_valve_state.set(valve_states[0])  # Set the default value

valve_state_menu = tk.OptionMenu(dam_frame, selected_valve_state, *valve_states)
valve_state_menu.grid(row=8, column=0, padx=10, pady=10)

# Drop-down menu for dam IDs
dam_ids = ["Dam1", "Dam2", "Dam3", "Dam4"]
selected_dam_id = tk.StringVar()
selected_dam_id.set(dam_ids[0])  # Set the default value

dam_id_menu = tk.OptionMenu(dam_frame, selected_dam_id, *dam_ids)
dam_id_menu.grid(row=8, column=1, padx=10, pady=10)

# Button to call API for changing valve state
button_change_valve = ttk.Button(dam_frame, text="Change Valve State", command=change_valve_state)
button_change_valve.grid(row=9, column=0, columnspan=2, padx=10, pady=10)


# Drop-down menu for valve states
pump_states = ["run", "stop"]
selected_pump_state = tk.StringVar()
selected_pump_state.set(pump_states[0])  # Set the default value

pump_state_menu = tk.OptionMenu(dam_frame, selected_pump_state, *pump_states)
pump_state_menu.grid(row=10, column=0, padx=10, pady=10)

# Drop-down menu for dam IDs
dam_ids2 = ["Dam1", "Dam2", "Dam3", "Dam4"]
selected_dam_id2 = tk.StringVar()
selected_dam_id2.set(dam_ids2[0])  # Set the default value

dam_id_menu2 = tk.OptionMenu(dam_frame, selected_dam_id2, *dam_ids2)
dam_id_menu2.grid(row=10, column=1, padx=10, pady=10)

# Button to call API for changing valve state
button_change_pump = ttk.Button(dam_frame, text="Change Pump State", command=change_pump_state)
button_change_pump.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

# Call the update_data function to start updating the GUI with real-time data
update_data()

# Start the main event loop
window.mainloop()
