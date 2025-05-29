import pytest
from app.repositories.parameter_repository import ParameterRepository

@pytest.fixture
def repo():
    return ParameterRepository()

def test_set_and_get(repo):
    repo.set("rate", 200)
    assert repo.get("rate") == 200

def test_all(repo):
    repo.set("a", 1)
    repo.set("b", 2)
    assert repo.all() == {"a": 1, "b": 2}