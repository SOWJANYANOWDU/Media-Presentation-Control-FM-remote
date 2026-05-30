# IR Remote Controller 🎮
I built this just for fun — tired of getting up every time to pause a video 
or go to the next slide when sitting far from device. So I made a remote do the job instead!
Now I can sit far from my laptop, control everything with the remote, 
and use my laptop like a TV. No more walking up to the keyboard! 

## What it does
- Control YouTube from far away — no need to touch the keyboard
- Control PowerPoint presentations without standing near the laptop
- Use your laptop comfortably like a TV from the couch

## Hardware I used
- Arduino 
- VS1838B IR Receiver
- Any IR Remote

## How it works
You press a button on the remote → Controller catches the signal and 
sends it to the PC → Python reads it and presses the matching keyboard key.
That's it!

## Built with
- Arduino + IRremote library
- Python + pyserial + pyautogui

*Just a fun project — because why get up when you have a remote? 😂*
