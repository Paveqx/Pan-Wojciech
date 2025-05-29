import httpx

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient()

    async def post_to_speech(self, text: str) -> bytes:
        resp = await self.client.post(f"{self.base_url}/api/to_speech", json={"text": text})
        resp.raise_for_status()
        return resp.content

    async def patch_parameter(self, name: str, value) -> dict:
        resp = await self.client.patch(f"{self.base_url}/api/set_parameter", json={"name": name, "value": value})
        resp.raise_for_status()
        return resp.json()