import socket
import pygame
from time import sleep
import threading

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)

locaddr = ('', 9000)
sock.bind(locaddr)


def recv():
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\nExit . . .\n')
            break


# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


class Drone:
    def __init__(self):
        self.takenoff = False
        self.speed = 60
        # self.battery = None
        self.__send_data('command')
        sleep(0.50)
        # self.battery = self.__send_data('battery?')
        # print('Battery: {}%'.format(self.battery))
        # sleep(0.50)
        # res = self.__send_data('speed {}'.format(self.speed))
        # if res == 'OK':
        #     print('Speed set to: {}%'.format(self.speed))
        sleep(0.50)

    def get_battery(self):
        return self.__send_data('battery?')

    def takeoff_land(self):
        if not self.takenoff:
            self.__send_data('takeoff')
            self.takenoff = True
        elif self.takenoff:
            self.__send_data('land')
            self.takenoff = False

    def forward(self):
        self.__send_data('forward {}'.format(self.speed))

    def back(self):
        self.__send_data('back {}'.format(self.speed))

    def left(self):
        self.__send_data('left {}'.format(self.speed))

    def right(self):
        self.__send_data('right {}'.format(self.speed))

    def __send_data(self, msg):
        # Send data
        msg = msg.encode(encoding="utf-8")
        sock.sendto(msg, tello_address)
        # return self.recv()

    # def recv(self):
    #     try:
    #         data, server = sock.recvfrom(1518)
    #         return data.decode(encoding="utf-8").rstrip()
    #     except Exception:
    #         print('Comms drop')


def main():
    print('\r\n\r\nTello Control.\r')
    print("\r\n       Takeoff / Land = SPACE "
          "\r\n       Control with arrows rotate = a/d,  up/down = w/s\r\n")
    print('Press ESC to quit.\r\n')

    screen, font = create_main_window()

    drone = Drone()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sock.close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('takeoff_land')
                    drone.takeoff_land()
                if event.key == pygame.K_UP:
                    print('forward')
                    drone.forward()
                if event.key == pygame.K_DOWN:
                    print('back')
                    drone.back()
                if event.key == pygame.K_LEFT:
                    print('left')
                    drone.left()
                if event.key == pygame.K_RIGHT:
                    print('right')
                    drone.right()

        #     pygame.display.flip()

        # try:
        #     hud_color = (230, 50, 0)
        #     hud = font.render('Battery: {}%'.format(drone.get_battery()), True, hud_color)
        #     screen.blit(hud, (20, 20))
        # except:
        #     pass

        # pygame.display.flip()

    print('Done')


def create_main_window():
    pygame.init()
    size = (620, 480)
    screen = pygame.display.set_mode(size)

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)

    white = (255, 64, 64)
    screen.fill((white))

    img = pygame.image.load('images/arrow.jpg')
    screen.blit(img, (210, 250))

    img = pygame.image.load('images/clockwise.png')
    img = pygame.transform.scale(img, (100, 100))
    screen.blit(img, (100, 200))

    forward = myfont.render("A", False, (0, 0, 0))
    screen.blit(forward, (145, 235))

    img = pygame.image.load('images/counterclockwise.png')
    img = pygame.transform.scale(img, (100, 100))
    screen.blit(img, (420, 200))

    forward = myfont.render("D", False, (0, 0, 0))
    screen.blit(forward, (465, 235))

    forward = myfont.render('Forward', False, (0, 0, 0))
    screen.blit(forward, (275, 255))

    forward = myfont.render('Back', False, (0, 0, 0))
    screen.blit(forward, (290, 415))

    forward = myfont.render('Left', False, (0, 0, 0))
    screen.blit(forward, (160, 370))

    forward = myfont.render('Right', False, (0, 0, 0))
    screen.blit(forward, (415, 370))

    pygame.display.flip()

    return screen, myfont


if __name__ == '__main__':
    main()
