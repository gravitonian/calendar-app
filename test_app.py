import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_event(client):
    response = client.post('/events', json={"name": "Meeting", "date": "2024-03-15"})
    assert response.status_code == 201
    assert response.get_json() == {"message": "Event added successfully!"}

def test_list_events(client):
    # Add an event first
    client.post('/events', json={"name": "Meeting", "date": "2024-03-15"})
    
    response = client.get('/events')
    assert response.status_code == 200
    assert len(response.get_json()) > 0
    assert response.get_json()[0]["name"] == "Meeting"
