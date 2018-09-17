from socketIO_client_nexus import SocketIO, LoggingNamespace
import json
import time
import random
import math

sock_client = SocketIO('localhost', 3000, LoggingNamespace)

i = 0

while True:
    
    arr = [10,20,30,40,50]
    x_1, x_2, x_3 = arr[i], arr[4-i], 50
    y_1, y_2, y_3 = arr[i], arr[4-i], 30
    hand1_x_1, hand1_y_1 = x_1 - 5, y_1 + 5
    hand2_x_1, hand2_y_1 = x_1 + 30, y_1 + 5
    
    hand1_x_2, hand1_y_2 = x_2 - 5, y_2 + 5
    hand2_x_2, hand2_y_2 = x_2 + 30, y_2 + 5

    sock_client.emit('messages',
                     json.dumps([
                        {'person_id': 'Billy', 'x': x_1, 'y': y_1, 'hand1_x': hand1_x_1, 'hand1_y': hand1_y_1, 'hand2_x': hand2_x_1, 'hand2_y': hand2_y_1},
                        {'person_id': 'Tommy', 'x': x_2, 'y': y_2, 'hand1_x': hand1_x_2, 'hand1_y': hand1_y_2, 'hand2_x': hand2_x_2, 'hand2_y': hand2_y_2},
                        {'person_id': 'Eric', 'x': x_3, 'y': y_3}
                     ]))
    i += 1
    if i > 4:
        i = 0

    time.sleep(1)