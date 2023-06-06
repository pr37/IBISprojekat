import tkinter as tk
from tkinter import ttk
import socket


def flowsensorBTN(apistr):
    result = client_call(apistr)  # Call the function
    result_label.config(text=result)  # Update the label with the returned string

def client_call(api_string):
    HOST, PORT = "localhost", 9999
    #HOST, PORT = "192.168.10.10", 9999

    #LIST OF API CALLS
    get_flow = bytes(api_string.encode())

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))

        sock.sendall(get_flow)
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


result_label = tk.Label(window, text="")
result_label.grid(row=1, column=0, padx=10, pady=10)
button = tk.Button(window, text="Get All Flow Sensor Readings", command=flowsensorBTN("GET FLOW_SENSOR ALL"))
button.grid(row=0, column=0, padx=10, pady=10)


# Start the main event loop
window.mainloop()
