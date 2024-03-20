### WebSocket Communication Benchmarking and Visualization
This project includes scripts for benchmarking WebSocket communication performance using various Python frameworks (FastAPI and Tornado) and visualizing the results using Matplotlib.

## Files:
***fastapi-wc.py***: Script for benchmarking WebSocket communication using FastAPI framework. It simulates multiple clients sending messages to a WebSocket server and calculates latency and throughput.

***fastapi-ws.py***: FastAPI WebSocket server script that echoes back received messages.

***tornado-wc.py***: Benchmarking script for WebSocket communication using Tornado framework. Similar to FastAPI, it measures latency and throughput of WebSocket communication.

***tornado-ws.py***: Tornado WebSocket server script that echoes back received messages.

***draw_plot.py***: Script to visualize the benchmarking results. It reads data from an Excel file containing latency measurements, applies moving average for smoothing, and plots the data using Matplotlib.

## Instructions:
Navigate to the directory where your virtual environment is located. You can find it at:  
```C:\.....\.....\venv\Scripts>``` 

Run the following command:   
```activate```  

Run the WebSocket servers ***(fastapi-ws.py or tornado-ws.py)*** on the desired port.  

* To run the FastAPI server, use the following command in the created new terminal:  
```uvicorn fastapi-ws:app --reload```   

* To run the Tornado server, use the following command in the created new terminal:  
```python tornado-ws.py```   
 
Execute the benchmarking scripts ***(fastapi-wc.py or tornado-wc.py)*** to simulate multiple clients sending messages to the server.   

* To run the FastAPI client, use the following command in the created new terminal:  
```python fastapi-wc.py```   

* To run the Tornado client, use the following command in the created new terminal:  
```python tornado-wc.py```   

Once benchmarking is complete, ***run draw_plot.py*** to visualize the latency measurements. Use the following command in the created new terminal 
```python draw_plot.py```   

## Dependencies:
FastAPI (for FastAPI scripts)
Tornado (for Tornado scripts)
Websockets (for FastAPI benchmarking)
Pandas (for data manipulation)
Matplotlib (for data visualization)

## Usage:
Ensure you have the required dependencies installed (pip install -r requirements.txt). Modify the server address and parameters such as message size and number of clients/messages per client as needed in the benchmarking scripts. Adjust the window size for moving average smoothing in draw_plot.py if necessary.
