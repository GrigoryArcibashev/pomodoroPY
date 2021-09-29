from time import sleep
from winsound import Beep

def start_timer(seconds):
    while seconds > 0:
        print(f'\r>>> {seconds // 60:02} : {seconds % 60:02}', end='')
        sleep(1)
        seconds -= 1

def beep():
    Beep(2500, 1000)

def main():
    while True:
        inp = str()
        while inp.lower() != 'y':
            inp = input('\n>>> Do you want to start the timer? (Y): ')
        start_timer(25 * 60)
        print('\n>>> Rest')
        start_timer(5 * 60)
        beep()


if __name__ == '__main__':
    main()