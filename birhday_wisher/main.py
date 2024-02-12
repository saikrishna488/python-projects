import pandas as pd
import datetime as dt
from email.message import EmailMessage
from password import password
import ssl
import smtplib
import pywhatkit as wpk

sender = "saikrishnaunique01@gmail.com"

# loading dataset
def load_dataset(path):
    data = pd.read_csv(path)
    return data

# todays date
def today():
    date = dt.datetime.now().strftime("%d-%b")
    year = dt.datetime.now().strftime("%Y")
    return date,year

#send message
def mail(receiver,subject,body):
    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as sm:
        sm.login(sender,password)
        sm.sendmail(sender,receiver,em.as_string())

# send whatsapp message
def send_Message(num,msg):
    wpk.sendwhatmsg('+'+str(num), msg,12,0,5)

# checking birthday
def birthday_check(data,today,year):
    for index,item in data.iterrows():
        day = item['Birthday']
        if day == today and str(year) not in str(item['Year']):
            print(item['Email'])
            mail(item['Email'],"Happy birthday "+item['Name'],item['Message'])
            send_Message(item['Number'],item['Message'])
            data['Year'] = data['Year'].astype(str)
            yr = data.at[index,'Year']
            data.at[index,'Year'] = str(yr) + ','+ str(year)

data = load_dataset("dataset.csv")
date,year = today()
birthday_check(data,date,year)
data.to_csv("dataset.csv",index=False)
