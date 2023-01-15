import requests

class SMS:
    def SendSms(phone_ip, port, number, message, auth_token):
        url = f"http://{phone_ip}:{port}"
        data = {"number": str(number), "message": str(message), "Authorization": str(auth_token)}
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        print(data)
        print(response.status_code)
        print(response.text)
        return response.status_code
