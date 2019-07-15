# BandWidth-Stealer

## Problem :
Are you in college and living in hostel??
Is there a wifi which require loginng in before you can download anything??
Do you want to download anything without logging in since it restricts the speed??

## Solution :
Step 1: Download the python script  
Step 2: Open it in any editor, and edit the url with your login gateway and edit ssid and name of your wifi there.  
Step 3: After saving it. Run it and enjoy downloading.  
P.S. : I've tested it on my college wifi router and used Torrents for downloading and it worked great and I'm using it  
       since.  

## How it works ??
When the wifi is connected to your system, the router sends some of the BandWidth to open the login gateway,  
So, I created a script which connects to the respective wifi and keep opening that login page at particular time interval,  
during which torrent downloader picks up that BandWidth to download your file.  
But, sometime the router disconnects itself because of opening the login gateway so many time.  
That is why script has cmd command which help the system to remain connected to the WIFI network.  
