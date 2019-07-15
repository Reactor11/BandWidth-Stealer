import webbrowser # Open
import time
import os
jio = 'https://jionet2.jio.in:8443'
count=0
tim = 0
while(1):
    count=count+1
    print(f"Count : {count}")
    webbrowser.open_new_tab(jio)
    webbrowser.open_new_tab(jio)
    webbrowser.open_new_tab(jio)
    time.sleep(30)
    tim = tim+30
    if(tim % 600 == 0):
        os.system('netsh wlan connect ssid=JioNet@LPU name=JioNet@LPU')
        print("Connecting WIFI.")
    os.system('taskkill /im chrome.exe /f')
    time.sleep(5)