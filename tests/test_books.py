from fastapi.testclient import TestClient
from src.app import app
from src.models import book


root_url =  "/api/v1/books"

#Test GET endpoint for a 200 status code
def test_get_book(client,test_book):
    response = client.get(f"{root_url}/1")
    print(response)

    assert response.status_code == 200  
    assert test_book["title"] == "Deep Work"
    assert test_book['author'] == "Cal Newport"

#Test DELETE endpoint for a 204 status code
def test_delete_book(client,test_book):
    response = client.delete(f"{root_url}/1")
    assert response.status_code == 204