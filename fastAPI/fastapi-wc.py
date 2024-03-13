import asyncio
import websockets
import time

async def send_messages():
    uri = "ws://localhost:8000/ws"  # Change this to your server address
    async with websockets.connect(uri) as websocket:
        message_id = 1;
        while True:
            message = str(message_id) + ". Message"
            message_id += 1
            
            #if message.lower() == 'exit':
            #    break
            
            start_time = time.time()

            await websocket.send(message)
            response = await websocket.recv()

            end_time = time.time()
            if end_time - start_time != 0:
                print("Elapsed Time:", end_time - start_time)

            #print("Received from server:", response)

asyncio.run(send_messages())
