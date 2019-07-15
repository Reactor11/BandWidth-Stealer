import webbrowser # This module open new tab in you default web browser.
import time # This module for sleep function.
import os # This module to run CMD commands.
url = 'https://jionet2.jio.in:8443' # Edit this url with your wifi login gateway url.
count = 0 # Counts how many times web browser has been opened.
tim = 0
print("------------------Firing Up The Stealer------------------")
while(1):
    count=count+1
    print(f"Count : {count}")
    webbrowser.open_new_tab(url) # Opens new tab in your browser
    webbrowser.open_new_tab(url)
    webbrowser.open_new_tab(url)
    time.sleep(30) # Sleeps for 30 Seconds
    tim = tim+30
    if(tim % 600 == 0):
        # Edit your ssid and name of the wifi here.
        # Connects to the wifi specified if the router disconnects your pc automatically itself.
        # Runs CMD command.
        os.system('netsh wlan connect ssid=JioNet@LPU name=JioNet@LPU')
        print("Connecting WIFI.")
    # Runs CMD command to kill the browser so that the program can run again automatically.
    os.system('taskkill /im chrome.exe /f')
    time.sleep(5)
