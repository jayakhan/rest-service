import json
import pytest
import sys
sys.path.append('/Users/zayakhan/Dev/content-extract-v1')
from main import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_research_materials(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = type(json.loads(res.get_data()))
    assert expected == dict