import zmq
from threading import Thread

## Message subscriber
class MessageSUB(Thread):
    def __init__(self,callback,topic):
        super().__init__()
        # variables
        self.topic = topic
        self.callback = callback

        # zmq LIB
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.setsockopt_string(zmq.SUBSCRIBE,"")
        self.socket.connect("ipc:///tmp/"+ self.topic) 


    def run(self):        
        while True:
            msg = self.socket.recv()
            self.callback(msg)

            
## Message publisher
class MessagePUB():
    def __init__(self,topic):
        # variables
        self.topic = topic
        
        # zmq LIB
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("ipc:///tmp/"+self.topic)

    def pub(self,msg):
        self.socket.send_string("%s" % msg)


