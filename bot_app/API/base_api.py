from aiohttp import ClientSession


class ApiClient:
    def __init__(self):
        self.session = ClientSession()

    async def post(self, endpoint: str, payload: dict):
        async with self.session.post(endpoint, json=payload) as response:
            return await response.json()

    async def close(self):
        await self.session.close()