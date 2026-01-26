import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.db.database import Base, engine


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """
    Create all tables before tests.
    """
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)
