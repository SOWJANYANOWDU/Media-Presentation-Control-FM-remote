import serial
import pyautogui

# Open the correct COM port (check Arduino IDE, e.g., COM5)
arduino = serial.Serial('COM5', 9600)

# Remote button address codes
CODES = {
    "FE017F80": "PLAY_PAUSE",   # Pause/Resume
    "F9067F80": "VOL_UP",       # Volume Up
    "FA057F80": "VOL_DOWN",     # Volume Down
    "FC037F80": "FWD",          # Forward
    "FD027F80": "BACK",         # Backward
    "E11E7F80": "MUTE",         # Mute
    "ED127F80": "STOP",         # Power button → Stop video
    "E51A7F80": "MODE"          # Mode button (toggle fullscreen/default)
}

# To keep track of current mode
mode_state = 0  # 0=Default, 1=Fullscreen

print("Ready: Use your remote to control YouTube")

while True:
    if arduino.in_waiting > 0:
        code = arduino.readline().decode().strip().upper()

        if code in CODES:
            action = CODES[code]

            if action == "PLAY_PAUSE":
                pyautogui.press("space")
                print("Play/Pause toggled")

            elif action == "VOL_UP":
                pyautogui.press("up")  # Increase volume
                print("Volume Up")

            elif action == "VOL_DOWN":
                pyautogui.press("down")  # Decrease volume
                print("Volume Down")

            elif action == "FWD":
                pyautogui.press("l")  # Forward 10 sec
                print("Forward Video")

            elif action == "BACK":
                pyautogui.press("j")  # Backward 10 sec
                print("Backward Video")

            elif action == "MUTE":
                pyautogui.press("m")  # Mute/Unmute
                print("Mute/Unmute")

            elif action == "STOP":
                pyautogui.press("0")  # Restart video (Stop simulation)
                print("Stopped/Restarted Video")

            elif action == "MODE":
               
                if mode_state == 0:  # Switch to Fullscreen
                    pyautogui.press("f")
                    print("Switched to Fullscreen")
                    mode_state = 1
                else:  # Switch to Default
                    pyautogui.press("esc")
                    print("Switched to Default View")
                    mode_state = 0















# import serial
# import pyautogui

# # Open the correct COM port (check Arduino IDE, e.g., COM5)
# arduino = serial.Serial('COM5', 9600)


# CODES = {
#     "FE017F80": "START",    # Play/Pause → Start slideshow
#     "FC037F80": "NEXT",     # Forward → Next slide
#     "FD027F80": "PREV",     # Backward → Previous slide
#     "ED127F80": "EXIT",     # Power → Exit slideshow
#     "E51A7F80": "TOGGLE"    # Mode → Toggle black/white
# }
# print("Ready: Use your remote to control Slides")
# while True:
#     if arduino.in_waiting > 0:
#         code = arduino.readline().decode().strip().upper()

#         if code in CODES:
#             action = CODES[code]

#             if action == "START":
#                 pyautogui.press("f5")
#                 print("Slideshow started")

#             elif action == "NEXT":
#                 pyautogui.press("right")
#                 print("Next slide")

#             elif action == "PREV":
#                 pyautogui.press("left")
#                 print("Previous slide")

#             elif action == "EXIT":
#                 pyautogui.press("esc")
#                 print("Exited slideshow")

#             elif action == "TOGGLE":
#                 pyautogui.press("b")  # Black screen toggle
#                 print("Black screen toggled")


