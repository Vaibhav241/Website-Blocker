import time
from datetime import datetime as dt

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"] # Ad websites you want to block
start_hour=8 #You can change the time for which you want to block these websites
end_hour=16 #You can change the time for which you want to block these websites

while True:
    if (dt(dt.now().year,dt.now().month,dt.now().day,start_hour)) < dt.now() < (dt(dt.now().year,dt.now().month,dt.now().day,end_hour)):
        with open(hosts_path,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    data=redirect + " " + website + "\n"
                    file.write(data)
    else:
        with open(hosts_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(300)
