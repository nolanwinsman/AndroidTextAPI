from sendSMS import SMS
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    auth = os.environ['AUTH']
    phone_ip = os.environ['PHONE_IP']
    port = os.environ['PORT']

    if port == '' or phone_ip == '' or auth == '':
        print(f"Failed to load in .env\nMake sure .env is in the root folder following the specifications in the README")
        exit()
    
    print(f"Testing to send an SMS.\nThis will send an SMS message if all the information is correct")
    ip = input("Input Your Android Phone's IP Address\t")
    number = input("Input the phone number you want to send an SMS to\t")
    message = input("Input the message you want to send to {number}\t")
    print(f"Is all this information correct?\nAUTH={auth}\nPhone IP Address={phone_ip}\nPort Number={port}\nNumber message will be sent to={number}\nMessage recipient will receive={message}")
    yes_no = input(f"Input yes if all the information is correct and you want to send an SMS message to {number}\t")
    if yes_no.lower() == 'yes' or yes_no.lower() == 'y':
        responseCode, responseText = SMS.SendSms(phone_ip=phone_ip, port=port, number=number, message=message, auth_token=auth)
        if responseCode == 200:
            print(f"SMS successfully sent\n{responseText}")
        else:
            print(f"Failed to send SMS\nResponse Code={responseCode}\nResponse Text={responseText}")
    else:
        print("SMS Not sent")
    


if __name__ == "__main__":
    main()
