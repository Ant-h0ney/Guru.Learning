from pytest_voluptuous import S
from requests import Response

from api.schemas import Resource
from utils.base_sessions import reqres_session


def test_getting_list():
    result: Response = reqres_session().get(
        url=f'/api/unknown'
    )
    assert result.status_code == 200
    assert result.json() == S(Resource.list)
    assert result.json()["data"][1]["name"] == 'fuchsia rose'


def test_getting_single():
    unknown_id = 7
    result: Response = reqres_session().get(
        url=f'/api/unknown/{unknown_id}'
    )
    assert result.status_code == 200
    assert result.json() == S(Resource.single)
    assert result.json()["data"]["id"] == unknown_id


def test_getting_single_not_found():
    unknown_id = 666
    result: Response = reqres_session().get(
        url=f'/api/unknown/{unknown_id}'
    )
    assert result.status_code == 404
