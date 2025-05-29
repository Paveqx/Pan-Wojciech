import pytest
from app.services.tts_service import TtsService
from app.repositories.parameter_repository import ParameterRepository

class DummyRepo(ParameterRepository):
    def get(self, name):
        return super().get(name)

@pytest.fixture
def service(tmp_path):
    repo = DummyRepo()
    return TtsService(repo)

def test_synthesize_returns_bytes(service):
    data = service.synthesize("Hello world")
    assert isinstance(data, (bytes, bytearray))
    assert len(data) > 0