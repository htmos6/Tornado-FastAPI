from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connection established.")  # Print when socket is connected
    try:
        while True:
            data = await websocket.receive_bytes()
            # Echo back the received bytes
            await websocket.send_bytes(data)
    except WebSocketDisconnect:
        print("WebSocket disconnected.")
