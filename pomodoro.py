from time import sleep
from winsound import Beep


def start_timer(seconds: int):
    while seconds >= 0:
        print(f'\r>>> {seconds // 60:02} : {seconds % 60:02}', end='')
        sleep(1)
        seconds -= 1


def beep():
    Beep(2500, 1000)


def cycle(rest_in_sec: int):
    start_timer(25 * 60)
    beep()
    print('\n>>> Rest')
    start_timer(rest_in_sec)
    beep()


def main():
    cycle_count = 1
    while True:
        inp = str()
        while inp.lower() != 'y':
            inp = input('\n>>> Do you want to start the timer? (Y): ')
        cycle(5 * 60 if cycle_count != 0 else 30 * 60)
        cycle_count = (cycle_count + 1) % 4


if __name__ == '__main__':
    main()
