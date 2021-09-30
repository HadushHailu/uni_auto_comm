import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

    #Emit a message
    sio.emit('my_message', {'response': 'my response'}) 

def map_data(sid, data):
    print('Acknowledgment message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

sio.on('map_data', map_data)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 6000)), app)
