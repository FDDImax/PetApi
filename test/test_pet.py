from api import Pets
from data import LoginData

pet = Pets()
LD = LoginData()


def test_login_user():
    status_code = pet.login_user()[2]
    user_ID = pet.login_user()[1]
    user_token = pet.login_user()[0]
    assert status_code == 200
    assert user_token
    assert user_ID == 1872
    print()
    print(user_ID)
    print(user_token)

def test_creat_pet():
    res = pet.creat_pet()
    status_code = res[1]
    pet_Id = res[0]
    assert status_code == 200
    assert pet_Id
    print()
    print(pet_Id)
    print(status_code)


def test_get_users():
    res = pet.get_users()
    status_code = res[0]
    user_id = res[1]
    assert status_code == 200
    assert user_id
    print()
    print(status_code)
    print(user_id)


