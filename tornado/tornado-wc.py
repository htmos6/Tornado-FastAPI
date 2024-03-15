import websocket
import time
import threading
import os

class Client:
    def __init__(self, url, num_messages):
        self.url = url
        self.num_messages = num_messages
        self.ws = websocket.WebSocketApp(url,
                                          on_open=self.on_open,
                                          on_message=self.on_message,
                                          on_error=self.on_error,
                                          on_close=self.on_close)
        
        # Initialize variables to track message sending and latency
        self.sent_messages = 0
        self.total_latency = 0
        self.message = bytes([ord('X')] * 102400)  # 100KB message
        self.connection_established = False

    def on_open(self, ws):
        # WebSocket connection is established
        print(f"Socket connected")
        self.connection_established = True
        self.send_messages()

    def on_message(self, ws, message):
        # Message received, calculate latency and send more messages if needed
        self.end_time = time.time()
        latency = self.end_time - self.start_time
        self.total_latency += latency
        self.sent_messages += 1

        # If not all messages have been sent, send more
        if self.sent_messages < self.num_messages:
            self.send_messages()
        else:
            self.ws.close()

    def on_close(self, ws):
        pass

    def on_error(self, ws, error):
        print("Error:", error)

    def run(self):
        # Run WebSocket connection
        self.ws.run_forever()
    
    def send_messages(self):
        # Send messages if connection is established
        if not self.connection_established:
            print("Error: Connection not established.")
            return

        self.start_time = time.time()
        self.ws.send(self.message)

def connect_client(client):
    client.run()

if __name__ == "__main__":
    num_clients = 20  # Number of concurrent clients
    num_messages_per_client = 1000  # Number of messages each client sends
    clients = []

    total_latency = 0  # To store total latency from all clients

    # Create client instances and threads
    threads = []
    for i in range(num_clients):
        client = Client("ws://localhost:3000/", num_messages_per_client)
        clients.append(client)
        thread = threading.Thread(target=connect_client, args=(client,))
        threads.append(thread)

    # Start threads
    for thread in threads:
        thread.start()

    num_threads = threading.active_count()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Get number of threads and cores
    num_cores = os.cpu_count()
    print(f"Number of cores : {num_cores}")
    print(f"Number of threads utilized: {num_threads}")



    # Calculate total latency and messages sent
    for client in clients:
        total_latency += client.total_latency

    total_messages_sent = num_clients * num_messages_per_client


    # Calculate average latency
    average_latency = total_latency / total_messages_sent
    print("Average Latency:", average_latency, "seconds per message")

    # Calculate throughput in bits per second (bps)
    # Message size: 1 KB (1 KB = 8,192 bits)
    message_size_bits = 100 * 8192  # 100 KB to bits
    total_time_seconds = sum(client.total_latency for client in clients)
    throughput_bps = (total_messages_sent * message_size_bits) / total_time_seconds
    print("Throughput:", throughput_bps / 1000, "kbps")


"""
if __name__ == "__main__":
    num_clients = 20  # Number of concurrent clients
    num_messages_per_client = 1000  # Number of messages each client sends
    clients = []

    total_latency = 0  # To store total latency from all clients

    # Create client instances and threads
    threads = []
    for i in range(num_clients):
        client = Client("ws://localhost:3000/", num_messages_per_client)
        clients.append(client)
        thread = threading.Thread(target=connect_client, args=(client,))
        threads.append(thread)

    # Start threads
    for thread in threads:
        thread.start()

    num_threads = threading.active_count()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Get number of threads and cores
    num_cores = os.cpu_count()
    print(f"Number of cores : {num_cores}")
    print(f"Number of threads utilized: {num_threads}")



    # Calculate total latency and messages sent
    for client in clients:
        total_latency += client.total_latency

    total_messages_sent = num_clients * num_messages_per_client


    # Calculate average latency
    average_latency = total_latency / total_messages_sent
    print("Average Latency:", average_latency, "seconds per message")

    # Calculate throughput in bits per second (bps)
    # Message size: 1 KB (1 KB = 8,192 bits)
    message_size_bits = 100 * 8192  # 100 KB to bits
    total_time_seconds = sum(client.total_latency for client in clients)
    throughput_bps = (total_messages_sent * message_size_bits) / total_time_seconds
    print("Throughput:", throughput_bps / 1000, "kbps")

"""