import webbrowser, os, psutil, pyautogui, time
from pynput import keyboard

def check_power_state():
    if psutil.sensors_battery().power_plugged:
        # The computer is running on AC power
        return
    else:
        # The computer is running on battery power
        if psutil.sensors_battery().percent <= 20:
            
            # The battery is low, shut down the program
             os.system('shutdown /s')
             
def on_activate():
    # Sensed the hotkey pressed
    print('Global hotkey activated!')
    # Opens spotify web player
    webbrowser.open("https://open.spotify.com/")
    # Move to pause button location
    pyautogui.moveTo(960, 990)
    # Rough waiting site to load
    time.sleep(9)
    # Clicks the pause button
    pyautogui.click()

def for_canonical(f):
    return lambda k: f(l.canonical(k))


hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<ctrl>+<alt>+h'),
        on_activate)

with keyboard.Listener(on_press=for_canonical(hotkey.press),
    on_release=for_canonical(hotkey.release)) as l: 
    l.join()
    
    while True:
        
        if(count == 600):
            check_power_state()
            count = 0
            print("We are good")
        
        time.sleep(.1)
        count = count + 1
        

