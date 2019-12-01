import requests
from bs4 import BeautifulSoup
import smtplib
import time

print("Ctrl-C to Interrupt the Program")

#The website for tracking
URL='https://www.flipkart.com/realme-5s-crystal-blue-64-gb/p/itm592977b0ba210?pid=MOBFM2WZ9AZUPTTZ&srno=s_1_2&otracker=search&otracker1=search&lid=LSTMOBFM2WZ9AZUPTTZXXEDBC&fm=organic&iid=01312424-7f61-4ff2-b26e-ad6e0b5a7989.MOBFM2WZ9AZUPTTZ.SEARCH&ssid=ogx9ncula80000001574849370830&qH=6841e7f327cfede0'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"} #Find your user agent by typing My User Agent in Google

def check_availability():
    page=requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup = BeautifulSoup(soup1.prettify(), "html.parser")

    #title = soup.find(id= "productTitle")

    #print(soup.prettify())
    try:
        notify=soup.find("button", { "class": "_2AkmmA _3-iCOr wvj5kH"}) #Find the class/id/button using inspect option

        foo = None

        #print(type(notify))

        if type(foo) == type(notify.get_text()):
            send_mail()
        else:
            if notify.get_text().strip().upper()[0:9] == "NOTIFY ME":
                print("No Change")
            else:
                send_mail()
    except:
        print('except error')
        send_mail()
        
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587) #Client depending upon your mail
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('email','password') #I reccomend using 2-step password verification and use that password
    subject = "Realme 5s Now available"
    Body = "Check the Flipkart Link https://www.flipkart.com/realme-5s-crystal-blue-64-gb/p/itm592977b0ba210?pid=MOBFM2WZ9AZUPTTZ&srno=s_1_2&otracker=search&otracker1=search&lid=LSTMOBFM2WZ9AZUPTTZXXEDBC&fm=organic&iid=01312424-7f61-4ff2-b26e-ad6e0b5a7989.MOBFM2WZ9AZUPTTZ.SEARCH&ssid=ogx9ncula80000001574849370830&qH=6841e7f327cfede0"
    msg = f"Subject: {subject} \n\n{Body}"
    server.sendmail(
        "email",
        "recipent",
        msg
    )
    print("An Email has been sent")
    server.quit()

    
    
try:
    while True:
        check_availability()
        #time.sleep(15)
        time.sleep(60*60) #Code run every hour
except KeyboardInterrupt:
    print('interrupted!')
