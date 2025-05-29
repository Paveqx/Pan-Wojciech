import pytest
import asyncio
from presentation.cli_parser import get_parser
from services.client_service import ClientService
from api.api_client import ApiClient

class DummyApi:
    def __init__(self):
        self.calls = []
    async def post_to_speech(self, text):
        self.calls.append(('speak', text))
        return b'data'
    async def patch_parameter(self, name, value):
        self.calls.append(('param', name, value))
        return {name: value}

@pytest.fixture
def svc():
    return ClientService(DummyApi())

@pytest.mark.asyncio
async def test_speak(tmp_path, svc):
    # powinno utworzyć plik tymczasowy i odtworzyć
    await svc.speak("Hello")
    assert svc.api.calls[0] == ('speak', 'Hello')

@pytest.mark.asyncio
async def test_download(tmp_path, svc):
    path = tmp_path / "out.wav"
    await svc.download("Hello", str(path))
    assert path.read_bytes() == b'data'

@pytest.mark.asyncio
async def test_set_param(svc):
    res = await svc.set_param('rate', 120)
    assert res['rate'] == 120

def test_cli_parser():
    p = get_parser()
    args = p.parse_args(["-s", "in.txt", "-o", "out.wav"])
    assert args.source == "in.txt"
    assert args.output == "out.wav"