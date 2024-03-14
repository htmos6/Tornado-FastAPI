import websocket
import time
import xlsxwriter


class Client:
    def __init__(self, url):
        self.url = url
        self.ws = websocket.WebSocketApp(url,
                                        on_open=self.on_open,
                                        on_message=self.on_message,
                                        on_error=self.on_error,
                                        on_close=self.on_close)
        
        self.start_time = 0
        self.end_time = 0
        self.workbook = xlsxwriter.Workbook('C:/Users/Legion/Desktop/tankX/100KB-10kTimes.xlsx')
        self.worksheet = self.workbook.add_worksheet()

        self.sent_message = 0


    def on_open(self, ws):
        #print("WebSocket opened")
        message = bytes([ord('X')] * 102400)
        self.start_time = time.time()
        ws.send(message)

    def on_message(self, ws, message):
        self.end_time = time.time()
        #print("Elapsed Time:", self.end_time - self.start_time)

        self.save_elapsed_time(self.end_time - self.start_time)

        # Close WebSocket after sending 10 messages
        self.sent_message += 1
        if self.sent_message == 10_000:
            self.workbook.close()
            self.ws.close()

        self.on_open(self.ws)

    def on_close(self, ws):
        self.workbook.close()
        #print("WebSocket closed")

    def on_error(self, ws, error):
        print("Error:", error)

    def run_forever(self):
        self.ws.run_forever()

    def save_elapsed_time(self, time_difference):
        self.worksheet.write(self.sent_message - 1, 0, time_difference)


if __name__ == "__main__":
    #websocket.enableTrace(True)
    client = Client("ws://localhost:3000/")
    client.run_forever()
