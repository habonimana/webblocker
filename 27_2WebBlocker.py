
import time
from datetime import datetime as dt
# windows has a host file
# a host file store information of IP address and web link of website 
# we want to bloc
# the host file is located: C:\Windows\System32\drivers\etc
host_temp = "hosts"
host_path= "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = [
    "www.facebook.com","facebook.com",
    "instagram.com", "www.instagram.com", "web.whatsapp.com",
    "www.web.whatsapp.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,6) < dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,12):
        print("Working Hours....")
        with open(host_path,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " "+ website+"\n")
    else:
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0) # to put the cursor/pointer on the first line
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() # stops the loop from continuous writing of the host's contents

        print("Fun ours....")


    time.sleep(5)# the loop run every five seconds

