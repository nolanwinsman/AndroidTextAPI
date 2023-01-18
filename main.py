from sendSMS import SMS 
from dotenv import load_dotenv
from datetime import date
import os
import json
import logging

AUTH = ''
PHONE_IP = ''
PORT = ''


# Sets the directory to where main.py is
main_py_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_py_directory)

# create a logger with a name
logger = logging.getLogger('sms_log')
logger.setLevel(logging.DEBUG)

# create a file handler to write log
file_handler = logging.FileHandler('sms.log')
file_handler.setLevel(logging.DEBUG)

# create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(file_handler)



def checkJsonFiles(today):
    """Loops through every .json file inside the json folder
    """
    folder_path = 'json'
    if len(os.listdir(folder_path)) <= 1:
        print(f"There are no .json files inside the json/ folder")
        print("If you do have a single .json file inside the json/ folder and are still having this error, you might have accidentally deleted the .gitignore file")
        exit()
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            filepath = os.path.join(folder_path, filename)
            with open(filepath) as json_file:
                json_data = json.load(json_file)
                for d in json_data:
                    if d['date'] == today:
                        createSMS(d)
                    else:
                        print(f"today is not {d['date']} skipping {d}")

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
    responseCode, responseText = SMS.SendSms(phone_ip=PHONE_IP, port=PORT, number=number, message=message, auth_token=AUTH)
    # responseCode, responseText = 200, 'no response text' # use this line to test the code without actually sending an SMS
    if responseCode == 200:
        logger.info(f"Successfully sent {firstname} {lastname} {number} the message {message}")
    else:
        logger.error(f"Failed to send {firstname} {lastname} {number} the message {message} Response Code is {responseCode} Response Text is {responseText}")


def main():
    logger.info('running main')
    load_dotenv()
    global AUTH
    AUTH = os.environ['AUTH']
    global PHONE_IP
    PHONE_IP = os.environ['PHONE_IP']
    global PORT
    PORT = os.environ['PORT']
    if PORT == '' or PHONE_IP == '' or AUTH == '':
        print(f'Failed to load in .env\nMake sure .env is in the root folder following the specifications in the README')
        exit()
    # Gets today's date and removes the year. So the format is "01-15"
    todayDate = date.today()
    # converts today's date to the format "Month-Day" For example "01-15"
    today = f"{todayDate.strftime('%m')}-{todayDate.strftime('%d')}"
    print(f"Checking the json files for {today}")
    checkJsonFiles(today)


if __name__ == "__main__":
    main()
