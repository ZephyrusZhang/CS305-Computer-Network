import asyncio
import websockets


class DanmakuServer:
    def __init__(self):
        self.clients = set()
        self.danmaku = list()

    async def reply(self, websocket):
        self.clients.add(websocket)
        for danmaku in self.danmaku:
            await websocket.send(danmaku)
        # noinspection PyBroadException
        try:
            while True:
                msg = await websocket.recv()
                self.danmaku.append(msg)
                websockets.broadcast(self.clients, msg)
        except Exception:
            pass


if __name__ == "__main__":
    server = DanmakuServer()
    asyncio.get_event_loop().run_until_complete(websockets.serve(server.reply, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()
