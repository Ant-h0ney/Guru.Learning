from pytest_voluptuous import S
from requests import Response

from api.schemas import Login
from utils.base_sessions import reqres_session


def test_successful_login():
    password = 'cityslicka'
    email = 'eve.holt@reqres.in'
    result: Response = reqres_session().post(
        url="/api/login",
        json={"email": email, "password": password},
    )
    assert result.status_code == 200
    assert result.json() == S(Login.successful)


def test_unsuccessful_login():
    password = 'anypass'
    email = 'notreal@mail.kek'
    result: Response = reqres_session().post(
        url="/api/login",
        json={"email": email, "password": password},
    )
    assert result.status_code == 400
    assert result.json() == S(Login.unsuccessful)
