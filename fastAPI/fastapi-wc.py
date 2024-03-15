import asyncio
import websockets
import time
import threading
import os

class Client:
    def __init__(self, uri, num_messages_per_client, message_size_kb):
        self.uri = uri
        self.num_messages_per_client = num_messages_per_client
        self.message_size_kb = message_size_kb
        self.total_latency = 0

    async def send_messages(self):
        # Connect to the WebSocket server
        async with websockets.connect(self.uri) as websocket:
            
            # Loop for sending messages
            for _ in range(self.num_messages_per_client):
                # Generate message with specified size
                message = bytes([ord('X')] * self.message_size_kb)
                
                # Record start time
                start_time = time.time()

                # Send message to server
                await websocket.send(message)
                await websocket.recv()

                # Record end time and calculate latency
                end_time = time.time()
                self.total_latency += (end_time - start_time)
            
            # If you want to disconnect the client, call close()
            await websocket.close()

async def main():
    num_clients = 20 # Number of concurrent clients
    num_messages_per_client = 1000  # Number of messages each client sends
    message_size_kb = 102400  # 10 kb message
    uri = "ws://localhost:8000/ws"  # Change this to your server address
    clients = []

    # Create client instances
    for _ in range(num_clients):
        client = Client(uri, num_messages_per_client, message_size_kb)
        clients.append(client)
        await client.send_messages()

    # Calculate total latency and total messages sent
    total_latency = sum(client.total_latency for client in clients)
    total_messages_sent = num_clients * num_messages_per_client

    # Calculate average latency
    average_latency = total_latency / total_messages_sent
    print("Average Latency:", average_latency, "seconds per message")

    # Calculate throughput in bits per second (bps)
    message_size_bits = message_size_kb * 8  # Message size in bits
    throughput_bps = (total_messages_sent * message_size_bits) / total_latency
    print("Throughput:", throughput_bps / 1000, "kbps")
    print("Total Processing Time:", total_latency, "seconds")

if __name__ == "__main__":
    
    # Get number of threads and cores
    num_threads = threading.active_count()
    num_cores = os.cpu_count()
    print(f"Number of cores : {num_cores}")
    print(f"Number of threads utilized: {num_threads}")
    
    # where the event loop is created and run
    # returns to here while waiting messages
    asyncio.run(main())
