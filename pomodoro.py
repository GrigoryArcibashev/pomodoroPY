import os
import sys
import time
import winsound


SHORT_REST_TIME = 5 * 60
LONG_REST_TIME = 30 * 60
WORK_TIME = 25 * 60


def start_timer(seconds: int):
    print(f'\r>>> {seconds // 60:02} : {seconds % 60:02}', end='')
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
        print(f'\r>>> {seconds // 60:02} : {seconds % 60:02}', end='')


def cycle(rest_in_sec: int):
    start_timer(WORK_TIME)
    beep()
    print('\n>>> Rest')
    start_timer(rest_in_sec)
    beep()


def beep():
    winsound.Beep(2500, 1000)


def clear_screen():
    os.system('CLS')


def process_user_input():
    inp = str()
    while inp not in ('y', 'n'):
        inp = input('\n>>> Do you want to start the timer? (Y/N): ')
        if inp.isalpha():
            inp = inp.lower()
    if inp == 'y':
        clear_screen()
    else:
        shut_down()


def shut_down():
    print('Нажмите любую кнопку, чтобы завершить программу')
    input()
    sys.exit(0)


def main():
    cycle_count = 1
    while True:
        process_user_input()
        cycle(SHORT_REST_TIME if cycle_count != 0 else LONG_REST_TIME)
        cycle_count = (cycle_count + 1) % 4


if __name__ == '__main__':
    main()
