from pynput import keyboard
from pynput.keyboard import Key, Listener

# Declare global variable text to store the key values

# Define function onPress() with parameter key, to detect the key values on button press

    # Access text as global
    
    # Use keyboard.Key to compare the key pressed 
    # and accordingly append the characters to the text variable if its a special key
    
    # Return false if it is escape key
    
    # Else do an explicit conversion from the key object to a string and then append that to the string text.
    
    
    # print text    
    

# Define function onRelease() with one parameter key

    # Check if key is escape key
    
        # return False
        


# Create listeners to listen keyboard events that calls onPress and onRelease functions when on_press and on_release events occurs respectively

    # Print "!!! WELCOME TO KEYLOGGER APP !!!"
    
    # Print "!!! APP IS READY TO LISTEN THE KEYS !!!"
    
    # Call join() method from listener
    
