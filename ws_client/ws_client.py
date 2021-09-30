
import socketio
from multiprocessing import Process
import signal
import sys
import logging

## LOGGING INFO
logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(level=logging.INFO)


## Websocket client
class WebsocketClient():
    def __init__(self,ws_address,on_msg_callback = ""):
        # Variables
        self.ws_address = ws_address
        self.sio = ""
        self.ws_process = ""
        self.on_msg_callback = on_msg_callback

        # Signal handler
        signal.signal(signal.SIGINT, self.keyboard_interupt)
        
    def keyboard_interupt(self,signal, frame):
       self.ws_process.join()
        
    def on_connect(self):
        LOGGER.info("ws connected.")

    def on_message(self,msg):
        LOGGER.info("ws got msg: %s",msg)
        if self.on_msg_callback is not None:
            self.on_msg_callback(msg)
    
    def on_disconnect(self):
        LOGGER.info("ws diconnected.")

    def get_ws_sio(self):
        return self.sio

    def init_websocketio(self):
        sio = socketio.Client()
        # self.sio.reconnection = False
        sio.on("connect",self.on_connect)
        sio.on("disconnect",self.on_disconnect)
        sio.on('my_message', self.on_message)
        sio.connect(self.ws_address)
        return sio

    def start_it(self):

        # Thread webscoket io
        self.sio = self.init_websocketio()
        self.ws_process = Process(target=self.sio.wait)
        self.ws_process.start()

if __name__ == '__main__':
    ws_address = 'http://localhost:6000'
    app = WebsocketClient(ws_address)
    app.start_it()
    
