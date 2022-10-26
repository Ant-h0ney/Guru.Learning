from pytest_voluptuous import S
from requests import Response

from api.schemas import User
from utils.base_sessions import reqres_session


def test_getting_users_data():
    user_id = 11
    result: Response = reqres_session().get(
        url=f'/api/users/{user_id}'
    )
    assert result.status_code == 200
    assert result.json() == S(User.data)
    assert result.json()["data"]["id"] == user_id
