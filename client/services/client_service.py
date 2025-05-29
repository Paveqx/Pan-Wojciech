import tempfile
from playsound import playsound
from pathlib import Path

class ClientService:
    def __init__(self, api_client):
        self.api = api_client

    async def speak(self, text: str):
        data = await self.api.post_to_speech(text)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        tmp.write(data)
        tmp.flush()
        playsound(tmp.name)

    async def download(self, text: str, path: str):
        data = await self.api.post_to_speech(text)
        Path(path).write_bytes(data)

    async def from_file(self, src: str, dst: str):
        text = Path(src).read_text(encoding="utf-8")
        await self.download(text, dst)

    async def set_param(self, name: str, value):
        return await self.api.patch_parameter(name, value)