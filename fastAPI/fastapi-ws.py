from fastapi import FastAPI, WebSocket
import sys

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        print(len(data))
        await websocket.send_bytes(data)  # Echo back the received bytes