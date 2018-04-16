import socket
import threading
from time import sleep


class Drone:
    def __init__(self):
        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = ('192.168.10.1', 8889)
        self.sock.bind(('', 9000))

        self.takeoff = False
        self.speed = 60
        # self.battery = None
        self.__send_data('command')
        sleep(0.50)
        res = self.__send_data('speed {}'.format(self.speed))
        if res == 'OK':
            print('Speed set to: {}%'.format(self.speed))
        sleep(0.50)

    def close(self):
        self.sock.close()

    def get_battery(self):
        return self.__send_data('battery?')

    def get_time(self):
        return self.__send_data('time?')

    def takeoff_land(self):
        if not self.takeoff:
            self.__send_data('takeoff')
            self.takeoff = True
        elif self.takeoff:
            self.__send_data('land')
            self.takeoff = False

    def forward(self):
        self.__send_data('forward {}'.format(self.speed))

    def back(self):
        self.__send_data('back {}'.format(self.speed))

    def left(self):
        self.__send_data('left {}'.format(self.speed))

    def right(self):
        self.__send_data('right {}'.format(self.speed))

    def up(self):
        self.__send_data('up {}'.format(self.speed))

    def down(self):
        self.__send_data('down {}'.format(self.speed))

    def clockwise(self):
        self.__send_data('cw {}'.format(self.speed))

    def counterclockwise(self):
        self.__send_data('ccw {}'.format(self.speed))

    def __send_data(self, msg):
        # Send data
        msg = msg.encode(encoding="utf-8")
        self.sock.sendto(msg, self.tello_address)
        return self.recv()

    def recv(self):
        try:
            data, server = self.sock.recvfrom(1518)
            return data.decode(encoding="utf-8").rstrip()
        except Exception:
            print('Comms drop')

# # recvThread create
# recvThread = threading.Thread(target=recv)
# recvThread.start()
