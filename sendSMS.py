import requests

class SMS:
    def SendSms(phone_ip, port, number, message, auth_token):
        url = f"http://{phone_ip}:{port}"
        data = {"number": str(number), "message": str(message), "Authorization": str(auth_token)}
        headers = {'Content-type': 'application/json'}
        try:
            response = requests.post(url, json=data, headers=headers)
            return response.status_code, response.text
        except ConnectionError:
            return 500, "ConnectionError"


