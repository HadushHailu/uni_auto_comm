import zmq,time
from msg_ntk import Map2DDataPUB
from msg_ntk import Map2DDataSUB
from threading import Thread

def msg_pub():

    msg = "Hello Hadush!"
    pub = Map2DDataPUB()

    counter = 1

    while True:
        pub.pub("%s %d" % (msg, counter))
        print(" PUB %s %d" % (msg, counter))
        time.sleep(1)
        counter += 1

def msg_sub(msg):
    print("SUB %s" % msg)


if __name__ == "__main__":
    

    # MAP SUB
    map_sub = Map2DDataSUB(msg_sub)
    map_sub.start()

    # PUB
    th = Thread(target = msg_pub)
    th.start()
