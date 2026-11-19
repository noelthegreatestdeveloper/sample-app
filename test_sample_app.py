
from sample_app import sample


def test_homepage_loads():
    client = sample.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_homepage_returns_html():
    client = sample.test_client()
    response = client.get("/")
    assert response.content_type.startswith("text/html")
