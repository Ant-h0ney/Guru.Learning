from pytest_voluptuous import S
from requests import Response

from api.schemas import User
from utils.base_sessions import reqres_session


def test_creating_user():
    name = 'testers gonna test'
    job = 'its unbelievable'
    result: Response = reqres_session().post(
        url="/api/users",
        json={"name": name, "job": job},
    )
    assert result.status_code == 201
    assert result.json() == S(User.created)
    assert result.json()['name'] == name
    assert result.json()['job'] == job
