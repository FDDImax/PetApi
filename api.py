import json
import requests
#import self as self

from data import LoginData


# from dotenv import load_dotenv


# load_dotenv()
LD = LoginData()


class Pets:
    def __init__(self):
        self.base_url = "http://34.141.58.52:8000/"

    def login_user(self) -> json:
        # """запрос к сваггеру, чтобы получить токен пользователя при логине"""
        data = {
            "email": LD.VALID_EMAIL,
            "password": LD.VALID_PASSWORD
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        user_token = response.json()["token"]
        user_id = response.json()["id"]
        status_cod = response.status_code
        return user_token, user_id, status_cod

    def creat_pet(self) -> json:
        #"""создаёт питомца залогиненому юзеру"""
        user_id = self.login_user()[1]
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'
                   }
        data = {
            "name": "W1",
            "type": "cat",
            "age": 7,
            "gender": "Male",
            "owner_id": user_id,
        }
        response = requests.post(self.base_url + "pet", data=json.dumps(data), headers=headers)
        pet_id = response.json()["id"]
        status_cod = response.status_code
        return pet_id, status_cod

    def get_users(self) -> json:
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        response = requests.get(self.base_url + "users", headers=headers)
        status_code = response.status_code
        user_id = response.json()
        return status_code, user_id


#Pets().login_user()
#Pets().creat_pet()
#Pets().get_users()
