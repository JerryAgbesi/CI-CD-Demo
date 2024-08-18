from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from fastapi.testclient import TestClient
import os

from src.db.database import Base, get_db
from src.app import app

TEST_DATABASE_URL = f"postgresql://{os.environ['TEST_DB_USER']}:{os.environ['TEST_PASSWORD']}@{os.environ['TEST_DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"

engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture()
def test_book(client):
    response = client.post("/api/v1/books",json={
        "title":"Deep Work",
        "author":"Cal Newport",
        "isbn":"9781455563869"
          })
    
    new_book = response.json()
  
    assert response.status_code == 201 
    assert new_book["title"] == "Deep Work"
    assert new_book["id"] == 1
    return new_book