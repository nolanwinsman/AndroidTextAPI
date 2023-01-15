# Text API
 This is a project to convert your android device to function as an API that can send text messages from your number. 

## Setup

Note: This program only works with Android phones.

This program requires you to setup the Android app first. View [**this repository**](https://github.com/nolanwinsman/KotlinSMSAPIApp) to setup the App.

1. Create **.env** file in the root folder of this project with the following information. 
You should change your AUTH Token inside the Android app, but by default it is **123456789**

The PORT is also defaulted to **9000** This is not as important to change, but you can change it if you want.

You can find your phone's IP address in settings, about phone. Or you can open the App and it will display your IP address.

```sh
AUTH=123456789
PHONE_IP=<your phone's IP address>
PORT=9000
```

2. Run test.py to validate if you are able to send SMS messages. It will prompt
```sh
python test.py
```

3. If test.py successfully sends an SMS message, everything is setup correctly.

## Setting up for use with Automation

If you just want to send an SMS through code, you can copy the file sendSMS.py which has a class that allows you to send SMS.

main.py is setup to automatically send an sms message for every **json** object inside every **.json** file inside the **json/** folder.

Inside the root of this project, there is **example.json** This is the format your json files will need to follow.

```sh
{
"firstname":"Jake",
"lastname":"Smith",
"number":"123456789",
"date":"01-15",
"uppercase":"True",
"message":"Happy Hypothetical Birthday {name}"
}
```

Most of the format is self-explanatory. You will want to change the firstname and lastname to the recipient. 

The SMS is only sent if the date is equal to today's date. So if you run main.py on 01-15, it will send an SMS message to Jake Smith.

If you run main.py on 03-24, it will not send an SMS message to Jake Smith.

uppercase is a boolean on if the message will have the first name in all caps or not. So in this example where "uppercase":"True", the message will be 
Happy Hypothetical Birthday JAKE

Make sure the number is correct.
