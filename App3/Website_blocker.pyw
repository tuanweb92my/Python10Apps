import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com","vnexpress.net"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours......")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            # print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect +" "+website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            # print(content)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours....")


    time.sleep(5)
