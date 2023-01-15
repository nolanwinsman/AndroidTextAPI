from sendSMS import SMS 
from dotenv import load_dotenv
from datetime import date
import os
import json

AUTH = ''
PHONE_IP = ''
PORT = ''

def checkJsonFiles(today):
    folder_path = 'json'
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            filepath = os.path.join(folder_path, filename)
            with open(filepath) as json_file:
                json_data = json.load(json_file)
                for d in json_data:
                    if d['date'] == today:
                        print("IT's TODAY")
                        createSMS(d)
                    else:
                        print(f"\ntoday is not {d['date'] skipping {d}}\n"

def createSMS(d):
    number = d['number']
    if d['uppercase'] == "True":
        firstname = d['firstname'].upper()
    else:
        firstname = d['firstname']
    lastname = d['lastname']
    number = d['number']
    raw_message = d['message']
    message = raw_message.format(name=firstname)
    print(number)
    print(message)
    responseCode = SMS.SendSms(phone_ip=PHONE_IP, port=PORT, number=number, message=message, auth_token=AUTH)
    print(f"The response code is {responseCode}")

def main():
    load_dotenv()
    global AUTH
    AUTH = os.environ['AUTH']
    global PHONE_IP
    PHONE_IP = os.environ['PHONE_IP']
    global PORT
    PORT = os.environ['PORT']
    # Gets today's date and removes the year. So the format is "01-15"
    today = str(date.today())[5:]
    print(f"checking the json files for {today}")
    checkJsonFiles(today)
    # SMS.SendSms(phone_ip=phone_ip, port=port, number=number, message=message, auth_token=auth)


if __name__ == "__main__":
    main()
