import pygame
from control_window import Color, create_main_window
from drone import Drone


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
                drone.close()
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
                if event.key == pygame.K_w:
                    print('up')
                    drone.up()
                if event.key == pygame.K_s:
                    print('down')
                    drone.down()
                if event.key == pygame.K_a:
                    print('counterclockwise')
                    drone.counterclockwise()
                if event.key == pygame.K_d:
                    print('clockwise')
                    drone.clockwise()

        try:
            battery = font.render('Battery: {}%'.format(drone.get_battery()), True, Color.HUD)
            screen.blit(battery, (20, 20))

            time = font.render('Time: {}sec'.format(drone.get_time()), True, Color.HUD)
            screen.blit(time, (20, 40))
        except:
            pass

        pygame.display.flip()

    print('Done')


if __name__ == '__main__':
    main()
